/**
 * passport 单点登录模块入口文件
 * @author pooky@lagou.com
 * @date 2014-12-23
 * @dependency lazyload
 * @global window.PASSPORT
 */

/**
 * 使用需知：
 * 使用script标签引入：
 * <script
 *     id="_lgpassport_"
 *     data-css-site="1"
 *     data-css-popup="1"
 *     src="https://passport.lagou.com/static/js/passport.js"></script>
 *
 * @id 必须，使用此默认值即可
 * @data-css-site 是否加载site.css（如果所使用的业务页面已经加载了site.css，则请将它设
 *     置为0，节省流量）
 * @data-css-popup 是否加载和弹窗浮层相关的css（如果所使用的业务页面已经加载了弹窗的样式，
 *     则请将它设置为0，节省流量）
 *
 * 具体使用:
 *
 *   // 监听自动登录
 *   PASSPORT.on( 'autologin:succ', function ( data ) {
 *       alert( 'autologin:succ ' + data );
 *       window.location.reload();
 *   } );
 *   PASSPORT.on( 'autologin:fail', function ( data ) {
 *
 *   } );
 *
 *   // 监听弹窗登录
 *   PASSPORT.on( 'popuplogin:succ', function ( data ) {
 *       alert( 'popuplogin:succ ' + data );
 *       window.location.reload();
 *   } );
 *   PASSPORT.on( 'popuplogin:fail', function ( data ) {
 *
 *   } );
 *
 *   // 触发自动登录
 *   PASSPORT.auto();
 *
 *   // 触发弹窗登录
 *   PASSPORT.popup();
 *
 *   // 跨系统调用工具方法
 *
 *
 *   // 【直接手动触发，不建议直接调用】触发远程登录，采用回调函数方式
 *   // 在有远程调用的地方，请使用`PASSPORT.util.rpc`函数
 *   PASSPORT.remote( 'http://server123',
 *       // 成功
 *       function ( data ) {
 *           alert( 'remotelogin:succ ' + data );
 *       },
 *       // 失败
 *       function ( data ) {
 *           alert( 'remotelogin:fail ' + data );
 *       }
 *   );
 *
 * !!!有关跨站请求、跨域请求登录不同步的处理逻辑：
 *
 *  1.如果调用发现用户未在该系统登录，则返回:【这一步是在业务逻辑层做的判断】
 *   {
 *       "content": {
 *           "data": {
 *               "crossServiceUrl": "http://xxxx.xxxx.com/crossServiceAjaxRequest.html"
 *           },
 *           "rows": []
 *       },
 *       "message": "should redirect to crossServiceUrl",
 *       "state": 10001
 *   }
 *
 *   2.js创建一个隐藏iframe【此处只需调用PASSPORT.remoteLogin( service )】，传入service参数即可
 *   当状态码是10001时，前端用js创建一个隐藏的iframe：
 *   https://passport.lagou.com/ajaxLogin/login.html?
 *       service=ENCODE(上面得到的crossServiceUrl)&
 *       osc=ENCODE(回调方法名+参数)&
 *       ofc=ENCODE(回调方法名+参数)
 *
 *   3.如果用户登录成功，将回调2步传入的osc对应的方法【只需监听：remotelogin:succ/fail】
 *
 *   4.如果登录成功，js应再重新发起一次同样的请求。【此处应该和业务逻辑相关，PASSPORT不作处理】
 */

( function() {

    /**
     * 调试模式
     * @type {Boolean}
     */
    var DEBUG  = false;

    /**
     * 版本号
     * @type {String}
     */
    var VERSION = '1.0.2';

    /**
     * 需要获取到自己的id
     * @type {String}
     */
    var ID = '_lgpassport_';

    /**
     * 构建iframe的index
     *
     * @type {Number}
     */
    var IFRAMEINDEX = 0;

    /**
     * 用来保存回调函数，键名既是index
     *
     * @type {Object}
     */
    var CALLBACKS = {

        // 远程调用的回调
        remote: {
            // 以index为索引
            // 2: {
            //     succ: func..
            //     fail: func..
            // }
        }

    };

    /**
     * 当前执行的脚本元素
     * @type {[type]}
     */
    var CURRENTSCRIPT = document.getElementById( ID );

    /**
     * url正则匹配
     * @type {RegExp}
     */
    var REGEXPURL = /^(https?):\/\/((?:[\u4E00-\u9FA5a-z0-9.-]|%[0-9A-F]{2}){2,})(?::(\d+))?((?:\/(?:[a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(?:\?((?:[a-z0-9-._~!$&'()*+,;=:\/?@]|%[0-9A-F]{2})*))?(?:#((?:[a-z0-9-._~!$&'()*+,;=:\/?@]|%[0-9A-F]{2})*))?$/i;

    /**
     * 请求目标地址
     * @type {Object}
     */
    var REMOTE = {

        // 中心
        server: 'https://passport.lagou.com',

        // 弹框登录的提交地址
        poplogin: '/login/login.json',

        // 弹窗登录中转
        poptransfer: '/ajaxLogin/frameGrant.html',

        // 自动登录中转
        autologin: '/ajaxLogin/login.html'

    };

    /**
     * 后端返回的状态值map
     * @type {Object}
     */
    var STATEMAP = {

        240: '请输入常用邮箱地址',
        210: '请输入100字以内的邮箱地址',
        220: '请输入有效的邮箱地址，如：gogo@lagou.com',
        241: '请输入密码',
        211: '请输入6-16位密码，字母区分大小写',
        299: '您操作太频繁了,过一会儿再来吧!',
        400: '该帐号不存在或密码错误，请重新输入',
        401: '登录失败，该帐号已被禁用',
        500: '登录失败,系统内部异常',

        other: '网络异常，请刷新重试'

    };

    /**
     * 模版
     * @type {Object}
     */
    var TEMPLATES = {

    };

    /**
     * MD5加密盐
     * Vee added @2015-05-04
     * @type {string}
     */
    var SALT = 'veenike';

    /**
     * 动态加载的样式
     * @type {Array}
     */
    var CSS = {
        // 整站样式
        site: '/static/css/style.css',
        // 弹出层登录框样式
        popup: '/static/css/loginPop/css/loginPop.css'
    };

    /**
     * 动态加载的逻辑文件
     * @type {Object}
     */
    var JS = {
        // jquery $( 'body' ).hide
        jq: '/static/js/jquery-1.11.1.min.js',
        // $( 'body' ).validate
        jqv: '/static/js/jquery.validate.js',
        //lagou validat
        lagou: '/static/js/lagou.js',
        // $.colorbox
        cb: '/static/js/colorbox.min.js',
        // window.stringifyJSON
        jsf: '/static/js/stringifyJSON.min.js',

        //加载md5.js文件 add by vee 2015-05-04
        md5: '/static/js/md5.js'
    };

    function analyzeUri( config ) {

        var loc = top.location;
        var origin = {
            protocol: loc.protocol.substring( 0, loc.protocol.length - 1 ),
            hostname: loc.hostname,
            port: loc.port || '80' // 默认80端口
        };

        var targetMatches = REGEXPURL.exec( config.url );

        // 不为null，则说明有匹配【需要判断是否跨域】
        // 如果为null，则说明是不加域名的绝对地址请求，例如：'/a/c.json'【不用跨域】
        if ( targetMatches && targetMatches.length ) {
             var target = {
                protocol: targetMatches[ 1 ],
                hostname: targetMatches[ 2 ],
                port: targetMatches[ 3 ] || '80'
            };

            // 如果跨域
            if ( origin.protocol != target.protocol
               || origin.hostname != target.hostname
               || origin.port != target.port) {
                config.dataType = 'jsonp';
                config.jsonp = 'jsoncallback';
            }
        }

    }

    /**
     * 工具集
     * @type {Object}
     */
    var util = {

        /**
         * 跨系统调用[jsonp]
         *
         * @param {Object} opt 请求参数
         *
         * @param {string} opt.url 请求路径
         * @param {string} opt.type optional 请求方法 'GET/POST'，默认'POST'
         * @param {Object} opt.params 请求参数
         * @param {Function} opt.succ 成功
         * @param {Function} opt.fail 失败
         */
        rpc: function( opt ) {

            if ( !opt.url )
                return;

            opt.type || ( opt.type = 'POST' );
            opt.params || ( opt.params = { } );

            var me = arguments.callee;

            util.tinfo( 'Start passport.rpc: ' + opt.url );

            var config = {

                type: opt.type,
                data: opt.params,
                url: opt.url,
                dataType: 'json'
                // jsonp: 'jsoncallback'

            };

            // 分析url是否跨域
            analyzeUri( config );

            $.ajax( config ).done( function( result, textStatus, jqXHR ){

                util.tinfo( 'passport.rpc.succ: ' + textStatus );

                // 判断是不是跨系统，且未登录
                if ( result.state == '10001' ) {
                    var crossServiceUrl = result.content.data.crossServiceUrl.replace(/^https?\:/i, window.location.protocol); // 兼容 http/https

                    PASSPORT.remote(
                      crossServiceUrl,
                      // 成功
                      function ( data ) {
                          util.tinfo( 'passport.rpc.remote.succ' );
                          me( opt );
                      },
                      // 失败
                      function ( data ) {
                          util.tinfo( 'passport.rpc.remote.fail' );
                          opt.fail && opt.fail.apply( null, [ data ] );
                      }
                    );

                    return;
                }

                // 如果跨系统已经登录，则正常响应
                opt.succ && opt.succ.apply( null, arguments );

            } ).fail( function ( jqXHR, textStatus, errorThrown ) {
                util.tinfo( 'passport.rpc.fail: ' + textStatus );
                opt.fail && opt.fail.apply( null, arguments );
            } );

        },

        /**
         * 得到默认的请求url
         *
         * @param  {string} url    url
         * @param  {Object} params 参数
         */
        getTargetUrl: function( url, params ) {

            var pas = {
                fl: ( params.fl != undefined ? params.fl : true ),
                service: params.service,
                osc: params.osc,
                ofc: params.ofc,
                pfurl: document.URL
            };

            return url + '?' + $.param( pas );

        },

        //得到当前页面的url
        getCurEncodeUrl: function() {
            return encodeURIComponent( document.URL );
        },

        //创建iframe
        createIframe: function( id, encodeUrl ) {
            var iframe = '<iframe src="'
                + encodeUrl
                // + '" id="' + id
                // 每一个iframe要区分自己
                + '" id="' + id + '_' + IFRAMEINDEX
                + '" style="display:none;"></iframe>';
            $( 'body' ).append( iframe );

            // 当前构建完毕要自加
            IFRAMEINDEX ++;
        },
        // 请求器
        requester: function( params, callback ) {
            params.dataType = params.dataType || 'json';
            params.type = params.type || 'POST';
            params.data = params.data || {};
            $.ajax( params ).done( function( response ) {
                callback && callback( response );
            } );
        },

        /**
         * 简易字符串格式化
         */
        strFormat: function( source, opts ) {
            source = String( source );
            var data = Array.prototype.slice.call( arguments, 1 ),
                toString = Object.prototype.toString;
            if ( data.length ) {
                data = data.length == 1 ?
                    /* ie 下 Object.prototype.toString.call(null) == '[object Object]' */
                    ( opts !== null && ( /\[object Array\]|\[object Object\]/.test( toString.call( opts ) ) ) ? opts : data ) : data;
                return source.replace( /#\{(.+?)\}/g, function( match, key ) {
                    var replacer = data[ key ];
                    // chrome 下 typeof /a/ == 'function'
                    if ( '[object Function]' == toString.call( replacer ) ) {
                        replacer = replacer( key );
                    }
                    return ( 'undefined' == typeof replacer ? '' : replacer );
                } );
            }
            return source;
        },

        /**
         * 日志头设置
         * @type {String}
         */
        tipheader: 'Lagou Passport v' + VERSION + ' -> ',

        /**
         * 展示日志
         */
        tip: function () {
            if ( !DEBUG )
                return;
            var method = arguments[ 0 ];
            var args = Array.prototype.slice.call( arguments, 1 );
            console[ method ].apply( console, args );
        },

        tinfo: function ( msg ) {
            util.tip( 'info', util.tipheader + msg );
        }

    };

    util.tinfo( 'Enter passport...' );

    /**
     * 需要使用简易的资源加载器
     * lazyload 直接使用min模式
     */
    /*jslint browser: true, eqeqeq: true, bitwise: true, newcap: true, immed: true, regexp: false */

    /**
    LazyLoad makes it easy and painless to lazily load one or more external
    JavaScript or CSS files on demand either during or after the rendering of a web
    page.

    Supported browsers include Firefox 2+, IE6+, Safari 3+ (including Mobile
    Safari), Google Chrome, and Opera 9+. Other browsers may or may not work and
    are not officially supported.

    Visit https://github.com/rgrove/lazyload/ for more info.

    Copyright (c) 2011 Ryan Grove <ryan@wonko.com>
    All rights reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the 'Software'), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    @module lazyload
    @class LazyLoad
    @static
    */

    var LazyLoad = ( function( doc ) {
        // -- Private Variables ------------------------------------------------------

        // User agent and feature test information.
        var env,

            // Reference to the <head> element (populated lazily).
            head,

            // Requests currently in progress, if any.
            pending = {},

            // Number of times we've polled to check whether a pending stylesheet has
            // finished loading. If this gets too high, we're probably stalled.
            pollCount = 0,

            // Queued requests.
            queue = {
                css: [],
                js: []
            },

            // Reference to the browser's list of stylesheets.
            styleSheets = doc.styleSheets;

        // -- Private Methods --------------------------------------------------------

        /**
        Creates and returns an HTML element with the specified name and attributes.

        @method createNode
        @param {String} name element name
        @param {Object} attrs name/value mapping of element attributes
        @return {HTMLElement}
        @private
        */
        function createNode( name, attrs ) {
            var node = doc.createElement( name ),
                attr;

            for ( attr in attrs ) {
                if ( attrs.hasOwnProperty( attr ) ) {
                    node.setAttribute( attr, attrs[ attr ] );
                }
            }

            return node;
        }

        /**
        Called when the current pending resource of the specified type has finished
        loading. Executes the associated callback (if any) and loads the next
        resource in the queue.

        @method finish
        @param {String} type resource type ('css' or 'js')
        @private
        */
        function finish( type ) {
            var p = pending[ type ],
                callback,
                urls;

            if ( p ) {
                callback = p.callback;
                urls = p.urls;

                urls.shift();
                pollCount = 0;

                // If this is the last of the pending URLs, execute the callback and
                // start the next request in the queue (if any).
                if ( !urls.length ) {
                    callback && callback.call( p.context, p.obj );
                    pending[ type ] = null;
                    queue[ type ].length && load( type );
                }
            }
        }

        /**
        Populates the <code>env</code> variable with user agent and feature test
        information.

        @method getEnv
        @private
        */
        function getEnv() {
            var ua = navigator.userAgent;

            env = {
                // True if this browser supports disabling async mode on dynamically
                // created script nodes. See
                // http://wiki.whatwg.org/wiki/Dynamic_Script_Execution_Order
                async: doc.createElement( 'script' ).async === true
            };

            ( env.webkit = /AppleWebKit\//.test( ua ) ) || ( env.ie = /MSIE|Trident/.test( ua ) ) || ( env.opera = /Opera/.test( ua ) ) || ( env.gecko = /Gecko\//.test( ua ) ) || ( env.unknown = true );
        }

        /**
        Loads the specified resources, or the next resource of the specified type
        in the queue if no resources are specified. If a resource of the specified
        type is already being loaded, the new request will be queued until the
        first request has been finished.

        When an array of resource URLs is specified, those URLs will be loaded in
        parallel if it is possible to do so while preserving execution order. All
        browsers support parallel loading of CSS, but only Firefox and Opera
        support parallel loading of scripts. In other browsers, scripts will be
        queued and loaded one at a time to ensure correct execution order.

        @method load
        @param {String} type resource type ('css' or 'js')
        @param {String|Array} urls (optional) URL or array of URLs to load
        @param {Function} callback (optional) callback function to execute when the
          resource is loaded
        @param {Object} obj (optional) object to pass to the callback function
        @param {Object} context (optional) if provided, the callback function will
          be executed in this object's context
        @private
        */
        function load( type, urls, callback, obj, context ) {
            var _finish = function() {
                    finish( type );
                },
                isCSS = type === 'css',
                nodes = [],
                i, len, node, p, pendingUrls, url;

            env || getEnv();

            if ( urls ) {
                // If urls is a string, wrap it in an array. Otherwise assume it's an
                // array and create a copy of it so modifications won't be made to the
                // original.
                urls = typeof urls === 'string' ? [ urls ] : urls.concat();

                // Create a request object for each URL. If multiple URLs are specified,
                // the callback will only be executed after all URLs have been loaded.
                //
                // Sadly, Firefox and Opera are the only browsers capable of loading
                // scripts in parallel while preserving execution order. In all other
                // browsers, scripts must be loaded sequentially.
                //
                // All browsers respect CSS specificity based on the order of the link
                // elements in the DOM, regardless of the order in which the stylesheets
                // are actually downloaded.
                if ( isCSS || env.async || env.gecko || env.opera ) {
                    // Load in parallel.
                    queue[ type ].push( {
                        urls: urls,
                        callback: callback,
                        obj: obj,
                        context: context
                    } );
                } else {
                    // Load sequentially.
                    for ( i = 0, len = urls.length; i < len; ++i ) {
                        queue[ type ].push( {
                            urls: [ urls[ i ] ],
                            callback: i === len - 1 ? callback : null, // callback is only added to the last URL
                            obj: obj,
                            context: context
                        } );
                    }
                }
            }

            // If a previous load request of this type is currently in progress, we'll
            // wait our turn. Otherwise, grab the next item in the queue.
            if ( pending[ type ] || !( p = pending[ type ] = queue[ type ].shift() ) ) {
                return;
            }

            head || ( head = doc.head || doc.getElementsByTagName( 'head' )[ 0 ] );
            pendingUrls = p.urls.concat();

            for ( i = 0, len = pendingUrls.length; i < len; ++i ) {
                url = pendingUrls[ i ];

                if ( isCSS ) {
                    node = env.gecko ? createNode( 'style' ) : createNode( 'link', {
                        href: url,
                        rel: 'stylesheet'
                    } );
                } else {
                    node = createNode( 'script', {
                        src: url
                    } );
                    node.async = false;
                }

                node.className = 'lazyload';
                node.setAttribute( 'charset', 'utf-8' );

                if ( env.ie && !isCSS && 'onreadystatechange' in node && !( 'draggable' in node ) ) {
                    node.onreadystatechange = function() {
                        if ( /loaded|complete/.test( node.readyState ) ) {
                            node.onreadystatechange = null;
                            _finish();
                        }
                    };
                } else if ( isCSS && ( env.gecko || env.webkit ) ) {
                    // Gecko and WebKit don't support the onload event on link nodes.
                    if ( env.webkit ) {
                        // In WebKit, we can poll for changes to document.styleSheets to
                        // figure out when stylesheets have loaded.
                        p.urls[ i ] = node.href; // resolve relative URLs (or polling won't work)
                        pollWebKit();
                    } else {
                        // In Gecko, we can import the requested URL into a <style> node and
                        // poll for the existence of node.sheet.cssRules. Props to Zach
                        // Leatherman for calling my attention to this technique.
                        node.innerHTML = '@import "' + url + '";';
                        pollGecko( node );
                    }
                } else {
                    node.onload = node.onerror = _finish;
                }

                nodes.push( node );
            }

            for ( i = 0, len = nodes.length; i < len; ++i ) {
                head.appendChild( nodes[ i ] );
            }
        }

        /**
        Begins polling to determine when the specified stylesheet has finished loading
        in Gecko. Polling stops when all pending stylesheets have loaded or after 10
        seconds (to prevent stalls).

        Thanks to Zach Leatherman for calling my attention to the @import-based
        cross-domain technique used here, and to Oleg Slobodskoi for an earlier
        same-domain implementation. See Zach's blog for more details:
        http://www.zachleat.com/web/2010/07/29/load-css-dynamically/

        @method pollGecko
        @param {HTMLElement} node Style node to poll.
        @private
        */
        function pollGecko( node ) {
            var hasRules;

            try {
                // We don't really need to store this value or ever refer to it again, but
                // if we don't store it, Closure Compiler assumes the code is useless and
                // removes it.
                hasRules = !!node.sheet.cssRules;
            } catch ( ex ) {
                // An exception means the stylesheet is still loading.
                pollCount += 1;

                if ( pollCount < 200 ) {
                    setTimeout( function() {
                        pollGecko( node );
                    }, 50 );
                } else {
                    // We've been polling for 10 seconds and nothing's happened. Stop
                    // polling and finish the pending requests to avoid blocking further
                    // requests.
                    hasRules && finish( 'css' );
                }

                return;
            }

            // If we get here, the stylesheet has loaded.
            finish( 'css' );
        }

        /**
        Begins polling to determine when pending stylesheets have finished loading
        in WebKit. Polling stops when all pending stylesheets have loaded or after 10
        seconds (to prevent stalls).

        @method pollWebKit
        @private
        */
        function pollWebKit() {
            var css = pending.css,
                i;

            if ( css ) {
                i = styleSheets.length;

                // Look for a stylesheet matching the pending URL.
                while ( --i >= 0 ) {
                    if ( styleSheets[ i ].href === css.urls[ 0 ] ) {
                        finish( 'css' );
                        break;
                    }
                }

                pollCount += 1;

                if ( css ) {
                    if ( pollCount < 200 ) {
                        setTimeout( pollWebKit, 50 );
                    } else {
                        // We've been polling for 10 seconds and nothing's happened, which may
                        // indicate that the stylesheet has been removed from the document
                        // before it had a chance to load. Stop polling and finish the pending
                        // request to prevent blocking further requests.
                        finish( 'css' );
                    }
                }
            }
        }

        return {

            /**
            Requests the specified CSS URL or URLs and executes the specified
            callback (if any) when they have finished loading. If an array of URLs is
            specified, the stylesheets will be loaded in parallel and the callback
            will be executed after all stylesheets have finished loading.

            @method css
            @param {String|Array} urls CSS URL or array of CSS URLs to load
            @param {Function} callback (optional) callback function to execute when
              the specified stylesheets are loaded
            @param {Object} obj (optional) object to pass to the callback function
            @param {Object} context (optional) if provided, the callback function
              will be executed in this object's context
            @static
            */
            css: function( urls, callback, obj, context ) {
                load( 'css', urls, callback, obj, context );
            },

            /**
            Requests the specified JavaScript URL or URLs and executes the specified
            callback (if any) when they have finished loading. If an array of URLs is
            specified and the browser supports it, the scripts will be loaded in
            parallel and the callback will be executed after all scripts have
            finished loading.

            Currently, only Firefox and Opera support parallel loading of scripts while
            preserving execution order. In other browsers, scripts will be
            queued and loaded one at a time to ensure correct execution order.

            @method js
            @param {String|Array} urls JS URL or array of JS URLs to load
            @param {Function} callback (optional) callback function to execute when
              the specified scripts are loaded
            @param {Object} obj (optional) object to pass to the callback function
            @param {Object} context (optional) if provided, the callback function
              will be executed in this object's context
            @static
            */
            js: function( urls, callback, obj, context ) {
                load( 'js', urls, callback, obj, context );
            }

        };
    } )( this.document );

    /**
     * 事件处理器
     */
    var Emitter = (function () {

        /**
         * Emitter
         *
         * @exports Emitter
         * @constructor
         */
        function Emitter() {}

        /**
         * Emitter的prototype（为了便于访问）
         *
         * @inner
         */
        var proto = Emitter.prototype;

        /**
         * 获取事件列表
         * 若还没有任何事件则初始化列表
         *
         * @private
         * @return {Object}
         */
        proto._getEvents = function () {
            if (!this._events) {
                this._events = {};
            }

            return this._events;
        };

        /**
         * 获取最大监听器个数
         * 若尚未设置，则初始化最大个数为10
         *
         * @private
         * @return {number}
         */
        proto._getMaxListeners = function () {
            if (isNaN(this.maxListeners)) {
                this.maxListeners = 10;
            }

            return this.maxListeners;
        };

        /**
         * 挂载事件
         *
         * @public
         * @param {string} event 事件名
         * @param {Function} listener 监听器
         * @return {Emitter}
         */
        proto.on = function (event, listener) {
            var events = this._getEvents();
            var maxListeners = this._getMaxListeners();

            events[event] = events[event] || [];

            var currentListeners = events[event].length;
            if (currentListeners >= maxListeners && maxListeners !== 0) {
                throw new RangeError(
                    'Warning: possible Emitter memory leak detected. '
                    + currentListeners
                    + ' listeners added.'
               );
            }

            events[event].push(listener);

            return this;
        };

        /**
         * 挂载只执行一次的事件
         *
         * @public
         * @param {string} event 事件名
         * @param {Function} listener 监听器
         * @return {Emitter}
         */
        proto.once = function (event, listener) {
            var me = this;

            function on() {
                me.off(event, on);
                listener.apply(this, arguments);
            }
            // 挂到on上以方便删除
            on.listener = listener;

            this.on(event, on);

            return this;
        };

        /**
         * 注销事件与监听器
         * 任何参数都`不传`将注销当前实例的所有事件
         * 只传入`event`将注销该事件下挂载的所有监听器
         * 传入`event`与`listener`将只注销该监听器
         *
         * @public
         * @param {string=} event 事件名
         * @param {Function=} listener 监听器
         * @return {Emitter}
         */
        proto.off = function (event, listener) {
            var events = this._getEvents();

            // 移除所有事件
            if (0 === arguments.length) {
                this._events = {};
                return this;
            }

            var listeners = events[event];
            if (!listeners) {
                return this;
            }

            // 移除指定事件下的所有监听器
            if (1 === arguments.length) {
                delete events[event];
                return this;
            }

            // 移除指定监听器（包括对once的处理）
            var cb;
            for (var i = 0; i < listeners.length; i++) {
                cb = listeners[i];
                if (cb === listener || cb.listener === listener) {
                    listeners.splice(i, 1);
                    break;
                }
            }
            return this;
        };

        /**
         * 触发事件
         *
         * @public
         * @param {string} event 事件名
         * @param {...*} args 传递给监听器的参数，可以有多个
         * @return {Emitter}
         */
        proto.emit = function (event) {
            var events = this._getEvents();
            var listeners = events[event];
            var args = Array.prototype.slice.call(arguments, 1);

            if (listeners) {
                listeners = listeners.slice(0);
                for (var i = 0, len = listeners.length; i < len; i++) {
                    listeners[i].apply(this, args);
                }
            }

            return this;
        };

        /**
         * 返回指定事件的监听器列表
         *
         * @public
         * @param {string} event 事件名
         * @return {Array} 监听器列表
         */
        proto.listeners = function (event) {
            var events = this._getEvents();
            return events[event] || [];
        };

        /**
         * 设置监听器的最大个数，为0时不限制
         *
         * @param {number} number 监听器个数
         * @return {Emitter}
         */
        proto.setMaxListeners = function (number) {
            this.maxListeners = number;

            return this;
        };

        /**
         * 将Emitter混入目标对象
         *
         * @param {Object} obj 目标对象
         * @return {Object} 混入Emitter后的对象
         */
        Emitter.mixin = function (obj) {
            for (var key in Emitter.prototype) {
                obj[key] = Emitter.prototype[key];
            }
            return obj;
        };

        return Emitter;

    } )();

    /**
     * 判断是不是已经加载了jQuery
     */
    var Has$ = function () {

        var has = false;

        try {
            has = !!( $ && jQuery && $( 'body' ).hide );
        }
        catch( e ) {
            has = false;
        }

        return has;

    }();

    var HasValidate = function () {

           return !!( Has$ && $( 'body' ).validate );

    }();

    var HasCb = function () {

       return !!( Has$ && $.colorbox );

    }();

    var HasJsf = function () {

       return !!( window.stringifyJSON );

    }();

    var HasMD5 = function () {

       return !!( HasMD5 && md5 );

    }();
  var HasLagou = function () {

       return !!( HasLagou && lg );

    }();
    util.tinfo( 'Has$: ' + Has$ );
    util.tinfo( 'HasValidate: ' + HasValidate );
    util.tinfo( 'HasCb: ' + HasCb );
    util.tinfo( 'HasLagou: ' + HasLagou );
    util.tinfo( 'HasJsf: ' + HasJsf );
    util.tinfo( 'HasMD5: ' + HasMD5 );

    /**
     * 加载css资源
     */
    ( function () {

        var site = CURRENTSCRIPT.getAttribute( 'data-css-site' );
        var popup = CURRENTSCRIPT.getAttribute( 'data-css-popup' );
        site = site == undefined ? 1 : ( + site );
        popup = popup == undefined ? 1 : ( + popup );

        if ( site ) {
            util.tinfo( 'Load site style...' );
            LazyLoad.css( REMOTE.server + CSS.site, function() {
                util.tinfo( 'Load site style success!' );
            } );
        }


        if ( popup ) {
            util.tinfo( 'Load popup style...' );
            LazyLoad.css( REMOTE.server + CSS.popup, function() {
                util.tinfo( 'Load popup style success!' );
            } );
        }

    } )();

    var READY = false;

    /**
     * 加载js文件
     */
    ( function () {

        var need2get = { };
        !Has$ && ( need2get[ JS.jq ] = false );
        !HasValidate && ( need2get[ JS.jqv ] = false );
        !HasLagou && ( need2get[ JS.lagou ] = false );
        !HasCb && ( need2get[ JS.cb ] = false );
        !HasJsf && ( need2get[ JS.jsf ] = false );
        !HasMD5 && ( need2get[ JS.md5 ] = false );

        var judgeReady = function () {
            for ( var key in need2get ) {
                if ( !need2get[ key ] ) {
                    return false;
                }
            }
            return true;
        };

        var getR = function ( key ) {
            util.tinfo( 'Load ' + key + '...' );
            LazyLoad.js( REMOTE.server + key, function() {
                need2get[ key ] = true;
                util.tinfo( 'Load ' + key + ' success!' );
                // util.tinfo( JSON.stringify( need2get ) );
                judgeReady() && ready4Next();
            } );
        };

        for ( var key in need2get ) {
            getR( key );
        }

    } )();

    /**
     * 事件中转中心
     * @type {Emitter}
     */
    var emitterControler = new Emitter();

    /**
     * 资源准备完毕
     */
    function ready4Next() {

        util.tinfo( 'Resource Ready!' );

        READY = true;

    }

    /**
     * 因为要等待依赖资源加载完毕才可以调用某个函数，故设置此函数
     */
    var delayWrapper = function ( func ) {

        return function () {

            var delay = 70;

            var args = arguments;

            if ( !READY ) {
                window.setTimeout( function () {
                    args.callee.apply( null, args );
                }, delay );
            }
            else {
                // 资源准备就绪开始执行，参数直接传递至func
                func.apply( null, args );
            }

        };

    };

    /**
     * 登录弹窗
     */
    var loginPopup = function() {
       var url  = util.getCurEncodeUrl();
       var root = REMOTE.server;
       $.colorbox( {
           html: '<div id="loginPop" class="popup" style="height:240px;">' +
               '<form id="login_form_popup" action="javascript:;" method="post"  data-view="loginView">' +
               '<div data-propertyname="username" data-controltype="Phone"><input type="text" id="email" name="email" tabindex="1" placeholder="请输入已验证手机/邮箱"></div>' +
               '<div data-propertyname="password" data-controltype="Password"><input type="password" id="password" name="password" tabindex="2" placeholder="请输入密码"></div>' +
               '<div class="input_item clearfix"  data-propertyname="request_form_verifyCode" data-controltype="VerifyCode" style="display:none;clear: both;"><input type="text" class="input input_white fl" style="width:150px;font-size: 16px;display:block;" name="" placeholder="请证明你不是机器人" data-required="required" autocomplete="off" ><img src="" alt="" class="yzm"><a href="javascript:;" class="reflash"></a></div>'+
               '<label class="fl" for="remember" style="display:none"><input type="checkbox" id="remember"  value="" checked="checked" name="autoLogin"> 记住我</label>' +
               '<a class="fr" href="' + root + '/accountPwd/toReset.html">忘记密码？</a>' +
               '<div data-propertyname="submit" data-controltype="Botton"><input type="button" id="submitLogin" value="登 &nbsp; &nbsp; 录" data-lg-tj-id="1gC0" data-lg-tj-no="idnull" data-lg-tj-cid="idnull"></div>' +
               '</form>' +
               '<div class="login_right">' +
               '<div>还没有拉勾帐号？</div>' +
               '<a href="' + root + '/register/register.html" class="registor_now" data-lg-tj-id="1gD0" data-lg-tj-no="idnull" data-lg-tj-cid="idnull">立即注册</a>' +
               '<div class="login_others">使用以下帐号直接登录:</div>' +
               '<a href="' + root + '/oauth20/auth_sinaWeiboProvider.html?service=' + url + '" target="_blank" id="icon_wb" class="icon_wb" title="使用新浪微博帐号登录" data-lg-tj-id="1hw0" data-lg-tj-no="idnull" data-lg-tj-cid="idnull"></a>' +
               '<a href="' + root + '/oauth20/auth_qqProvider.html?service=' + url + '" class="icon_qq" id="icon_qq" target="_blank" title="使用腾讯QQ帐号登录" data-lg-tj-id="1hx0" data-lg-tj-no="idnull" data-lg-tj-cid="idnull"></a>' +
               '<a href="' + root + '/oauth20/auth_weixinProvider.html?service=' + url + '" class="icon_weixin" id="icon_weixin" target="_blank" title="使用微信帐号登录" data-lg-tj-id="1hy0" data-lg-tj-no="idnull" data-lg-tj-cid="idnull"></a>' +
               '</div>' +
               '</div>',
           title: '登录'
        } );

     /*   $( 'body' ).on( 'click', '#login_form_popup #submitLogin', function() {
            var form = $( 'body #colorbox #login_form_popup' );
            login_valid();
            var isValid = form.valid();
            if ( isValid ) {
                success( form );
            } else {
                return false;
            }
        } );*/
        var loginView = new lg.Views.BaseView({
        name: 'loginView',
        fields: [{
            name: 'username',
            validRules: [{
                    mode: 'require',
                    data: '',
                    message: '请输入已验证手机/邮箱',
                    trigger: 'blur'
                }, {
                    mode: 'pattern',
                    isUse: true,
                    status: false,
                    data:{phone:/^(0|86|17951)?((13[0-9]|15[012356789]|17[0135678]|18[0-9]|14[57])[0-9]{8})$/,email:/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))$/i},
                    message: '请输入有效的手机/邮箱'
                }

            ],
            controlType: "Phone"
        }, {
            name: 'password',
            validRules: [{
                mode: 'require',
                data: '',
                message: '请输入密码'
            }, {
                mode: 'pattern',
                data: '/^[\\S\\s]{6,16}$/',
                message: '请输入6-16位密码，字母区分大小写'
            }],
            controlType: "Password"
        }, {
            name: 'request_form_verifyCode',
            isVisible: false,
            validRules: [],
            from: 'register',
            url: 'https://passport.lagou.com/vcode/create',
            controlType: "VerifyCode"
        }, {
            name: 'submit',
            validRules: [],
            controlType: "Button",
            url: "/login/login.json",
            click: function(e) {
                var that = e;
                var params = that.parent.CollectData();
                var SALT = 'veenike';
                if (params.isValidate) {
                    params.password = md5(params.password);
                    params.password = md5(SALT + params.password + SALT);

                    var rem = $( '#remember', $( 'body #colorbox #login_form_popup') );

                    if ( rem.prop( "checked" ) ) {
                        rem.val( 1 );
                    } else {
                        rem.val( null );
                    }
                    var remember = rem.val();
                    var rememberMe = ( remember == undefined || remember == null )
                        ? false
                        : ( remember == 1 ? true : false );
                    params.rememberMe = rememberMe;

                    $.ajax({
                        url: that.control._option.url,
                        data: params,
                        url: REMOTE.server + REMOTE.poplogin,
                        dataType: 'jsonp',
                        jsonp: 'jsoncallback'
                    }).done(function(result) {
                        var stateList = {
                            1: {
                                message: "成功",
                                linkFor: 'password',
                                level: 'info'
                            },
                            210: {
                                message: "请输入有效的手机/邮箱",
                                linkFor: 'username',
                                level: 'error'
                            },
                            211: {
                                message: "请输入6-16位密码，字母区分大小写",
                                linkFor: 'password',
                                level: 'error'
                            },
                            220: {
                                message: "请输入有效的手机/邮箱",
                                linkFor: 'username',
                                level: 'error'
                            },
                            240: {
                                message: "请输入已验证手机/邮箱",
                                linkFor: 'username',
                                level: 'error'
                            },
                            241: {
                                message: "请输入密码",
                                linkFor: 'password',
                                level: 'error'
                            },
                            299: {
                                message: "你的操作太过频繁，请稍后再试",
                                linkFor: 'password',
                                level: 'error'
                            },
                            400: {
                                message: "帐号和密码不匹配",
                                linkFor: 'password',
                                level: 'error'
                            },
                            500: {
                                message: "登录失败,系统内部异常",
                                linkFor: 'password',
                                level: 'error'
                            },
                            10010: {
                                message: "验证码不正确",
                                linkFor: 'request_form_verifyCode',
                                level: 'error'
                            },
                            10011: {
                                message: "操作太频繁",
                                linkFor: 'password',
                                level: 'error'
                            },
                            10012: {
                                message: "系统错误",
                                linkFor: 'password',
                                level: 'error'
                            }
                        }
                        if (stateList[result.state]  && result.state != 1) {
                            that.parent.field[stateList[result.state].linkFor].showMessage({
                                message: stateList[result.state].message
                            });
                        }
                        if(result.state ==10010 && !that.parent.field['request_form_verifyCode'].getIsVisible()){
                            that.parent.field["request_form_verifyCode"].getVerifyCode();
                            that.parent.field["request_form_verifyCode"].setVisible(true);
                        }
                        if (stateList[result.state].level == "info" && result.state == 1) {
                            var turl = util.getTargetUrl( REMOTE.server + REMOTE.poptransfer, {
                                fl: '2',
                                service: document.URL,
                                osc: 'PASSPORT._pscb(' + IFRAMEINDEX + ')',
                                ofc: 'PASSPORT._pfcb(' + IFRAMEINDEX + ')'
                            } );
                            util.createIframe( 'popup_login_iframe', turl );

                        }else{
                            that.parent.field["request_form_verifyCode"].getVerifyCode();
                        }

                    });
                }
            }
        }]
    });
    };

    //验证成功之后执行
    function success( form ) {
        var rem = $( '#remember', form );
        if ( rem.prop( "checked" ) ) {
            rem.val( 1 );
        } else {
            rem.val( null );
        }
        var email    = $.trim( $( '#email', form ).val() );
        var password = $( '#password', form ).val();

        password = md5(password);
        password = md5(SALT + password + SALT);

        var remember = rem.val();
        var rememberMe = ( remember == undefined || remember == null )
            ? false
            : ( remember == 1 ? true : false );
        $( form ).find( ":submit" ).attr( "disabled", true );
        $.ajax( {
            type: 'POST',
            data: {
                username: email,
                password: password,
                rememberMe: rememberMe
            },
            url: REMOTE.server + REMOTE.poplogin,
            dataType: 'jsonp',
            jsonp: 'jsoncallback'
        } ).done( function( result ) {
            if ( result.state == 1 ) {
                var turl = util.getTargetUrl( REMOTE.server + REMOTE.poptransfer, {
                    fl: '2',
                    service: document.URL,
                    osc: 'PASSPORT._pscb(' + IFRAMEINDEX + ')',
                    ofc: 'PASSPORT._pfcb(' + IFRAMEINDEX + ')'
                } );
                util.createIframe( 'popup_login_iframe', turl );
            }
            else {
                var tips = STATEMAP[ result.state ] || STATEMAP.other;
                $( '#login_beError' ).text( tips ).show();
            }
            $( form ).find( ":submit" ).attr( "disabled", false );
        } );
    }

    /**
     * 登录验证器
     */
    function login_valid() {
        $( "#login_form_popup" ).validate( {
            onkeyup: false,
            focusCleanup: true,
            rules: {
                email: {
                    required: true,
                    email: true,
                    maxlength: 100
                },
                password: {
                    required: true,
                    rangelength: [ 6, 16 ]
                }
            },
            messages: {
                email: {
                    required: "请输入登录邮箱地址",
                    email: "请输入有效的邮箱地址，如：gogo@lagou.com",
                    maxlength: "请输入100字以内的邮箱地址"
                },
                password: {
                    required: "请输入密码",
                    rangelength: "请输入6-16位密码，字母区分大小写"
                }
            }

        } );
    }

    /**
     * 删除无用的iframe
     * @param  {string} type  类型
     * @param  {number} index 索引
     */
    function delIframe( type, index ) {

        var id = type + '_' + index;
        $( '#' + id ).remove();
        util.tinfo( 'Iframe ' + id + ' removed' );

    }

    /**
     * 使用PASSPORT全局变量对外
     * @type {Object}
     */
    window.PASSPORT = window.PASSPORT || {

        /**
         * 绑定自定义事件【针对`auto`，`popup`的监听器】
         * @param  {string} event    事件类型
         * @param  {Function} listener  监听器
         */
        on: function () {
            emitterControler.on.apply( emitterControler, arguments );
        },

        /**
         * 触发自动登录
         * @desc 监听事件[ autologin:xxx ]
         */
        auto: delayWrapper( function () {
            var turl = util.getTargetUrl(
                REMOTE.server + REMOTE.autologin,
                {
                    fl: '1',
                    service: document.URL,
                    osc: 'PASSPORT._ascb(' + IFRAMEINDEX + ')',
                    ofc: 'PASSPORT._afcb(' + IFRAMEINDEX + ')'
                }
            );
            util.createIframe( 'auto_login_iframe', turl );
        } ),

        /**
         * 以下两个为自动登录的回调
         *
         * @private
         * @param  {[type]} data [description]
         */
        _ascb: function ( index, data ) {
            util.tinfo( 'Call of PASSPORT._ascb' + index + ': ' + data );
            emitterControler.emit( 'autologin:succ', data );
            delIframe( 'auto_login_iframe', index );
        },
        _afcb: function ( index, data ) {
            util.tinfo( 'Call of PASSPORT._afcb' + index + ': ' + data );
            emitterControler.emit( 'autologin:fail', data );
            delIframe( 'auto_login_iframe', index );
        },

        /**
         * 可以被主动调用的登录弹窗
         */
        popup: delayWrapper( function () {
            loginPopup();
        } ),

        /**
         * 以下两个为弹窗登录的回调
         *
         * @private
         * @param  {[type]} data [description]
         */
        _pscb: function ( index, data ) {
            util.tinfo( 'Call of PASSPORT._pscb' + index + ': ' + data );
            emitterControler.emit( 'popuplogin:succ', data );
            delIframe( 'popup_login_iframe', index );
        },
        _pfcb: function ( index, data ) {
            util.tinfo( 'Call of PASSPORT._pfcb' + index + ': ' + data );
            emitterControler.emit( 'popuplogin:fail', data );
            delIframe( 'popup_login_iframe', index );
        },

        /**
         * 远程登录
         * @param  {string} server 响应出10001的接口url
         */
        remote: delayWrapper( function ( server, succ, fail ) {
            util.tinfo( 'Remote request: ' + server + ' '
                + succ + ' '
                + fail );
            // 放入回调
            CALLBACKS.remote[ IFRAMEINDEX ] = { };
            if ( succ ) {
                CALLBACKS.remote[ IFRAMEINDEX ].succ = succ;
            }
            if ( fail ) {
                CALLBACKS.remote[ IFRAMEINDEX ].fail = fail;
            }
            util.tinfo( 'Remote request put into callbacks: ' + JSON.stringify(
                CALLBACKS.remote ) );
            var turl = util.getTargetUrl(
                REMOTE.server + REMOTE.autologin,
                {
                    fl: '3',
                    service: server,
                    osc: 'PASSPORT._rscb(' + IFRAMEINDEX + ')',
                    ofc: 'PASSPORT._rfcb(' + IFRAMEINDEX + ')'
                }
            );
            util.createIframe( 'remote_login_iframe', turl );
        } ),

        /**
         * 以下两个为远程登录的回调
         *
         * @private
         * @param  {[type]} data [description]
         */
        _rscb: function ( index, data ) {
            util.tinfo( 'Call of PASSPORT._rscb' + index + ': ' + data );
            emitterControler.emit( 'remotelogin:succ', data );
            delIframe( 'remote_login_iframe', index );
            // 触发回调函数
            CALLBACKS.remote[ index ]
                && CALLBACKS.remote[ index ].succ
                && CALLBACKS.remote[ index ].succ( data );
        },
        _rfcb: function ( index, data ) {
            util.tinfo( 'Call of PASSPORT._rfcb' + index + ': ' + data );
            emitterControler.emit( 'remotelogin:fail', data );
            delIframe( 'remote_login_iframe', index );
            // 触发回调函数
            CALLBACKS.remote[ index ]
                && CALLBACKS.remote[ index ].fail
                && CALLBACKS.remote[ index ].fail( data );
        },

        util: {
            rpc: delayWrapper( util.rpc )
        }

    };

} )();
