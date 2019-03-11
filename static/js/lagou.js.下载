/**
 * Created by storm on 15/9/25.
 */

/** ----------------------------------------------------------------- start
 *命名空间
 *
 */
var lg = window.lg || {};
/**
 * lg={}
 * {
 *      Utils
 *      Widgets
 *      Views
 *      Models
 *      Cache
 *      TempletEngine
 *      Routers
 *      Events
 *      .
 *      .
 *      .
 * }
 */
if (!Array.prototype.indexOf)
{
  Array.prototype.indexOf = function(elt /*, from*/)
  {
    var len = this.length >>> 0;

    var from = Number(arguments[1]) || 0;
    from = (from < 0)
         ? Math.ceil(from)
         : Math.floor(from);
    if (from < 0)
      from += len;
    for (; from < len; from++)
    {
      if (from in this &&
          this[from] === elt)
        return from;
    }
    return -1;
  };
}
if(!String.prototype.trim){
    String.prototype.trim=function(){
　　    return this.replace(/(^\s*)|(\s*$)/g, "");
　　 }
　　 String.prototype.ltrim=function(){
　　    return this.replace(/(^\s*)/g,"");
　　 }
　　 String.prototype.rtrim=function(){
　　    return this.replace(/(\s*$)/g,"");
　　 }
}

lg.Event = lg.Event || {};

lg.Event._events = {};
lg.Event.on = function(eventName, data, func) {
    this._events[eventName] = this._events[eventName] || []
    this._events[eventName].push({
        data: data,
        func: func
    });
    return this;

}
lg.Event.un = function(eventName, func) {
    var events = this._events;

    // 移除所有事件
    if (0 === arguments.length) {
        this._events = {};
        return this;
    }

    var listeners = events[eventName];
    if (!listeners) {
        return this;
    }

    // 移除指定事件下的所有监听器
    if (1 === arguments.length) {
        delete events[eventName];
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

lg.Event.exec = function(eventName) {
    var events = this._events;
    var listeners = events[eventName];
    var args = Array.prototype.slice.call(arguments, 1);

    if (listeners) {
        listeners = listeners.slice(0);
        for (var i = 0, len = listeners.length; i < len; i++) {
            listeners[i].apply(this, args);
        }
    }
    return this;
};




lg.Cache = lg.Cache || {};
lg.Cache.Views = lg.Cache.Views || {};

/**-----------------------------------------------------------------  start
 * 公共工具箱
 */

lg.Utils = lg.Utils || {};
/**
 * lg.Utils={}
 * {
 *      getNewId()
 *      Formate()
 *      .
 *      .
 *      .
 * }
 */

/**
 * 判断对象val 是否等于 {}
 * @param val
 * @returns {boolean}
 */
lg.Utils.isNullObject = function(val) {
    if (typeof val === "object" && !(val instanceof Array)) {
        var hasProp = false;
        for (var prop in val) {
            hasProp = true;
            break;
        }
        return hasProp;
    }
}

//------------------------------------------------------------------  end


/**-----------------------------------------------------------------  start
 * 命名控件 - 控件
 */

lg.Widgets = lg.Widgets || {};

/**
 * 控件基础够着函数
 * @param options
 * @constructor
 */
lg.Widgets.BaseControl = function(options) {
    this._name = '';
    this._option = {};
    this.Event = lg.Event;
    this._data = {};
    this._value = '';
    this._isDirty = false;
    this._isValueField = true;
    this._data.valid = this._data.valid || {};
    this._data.valid.validResult = {};
    this._data.valid._map = {
        require: {
            mode: 'require',
            isUse: false,
            status: false,
            data: '',
            message: '必填',
            level:'3',
            trigger: []
        },
        re_pwd: {
            mode: 'repeat-password',
            isUse: false,
            status: false,
            data: '',
            message: '',
            level:'2',
            trigger: []
        },
        min_len: {
            mode: 'min-length',
            isUse: false,
            status: false,
            data: '',
            message: '最小长度',
            level:'1',
            trigger: []
        },
        max_len: {
            mode: 'max-length',
            isUse: false,
            status: false,
            data: '',
            message: '最大长度',
            level:'1',
            trigger: []

        },
        pattern: {
            mode: 'pattern',
            isUse: false,
            status: false,
            data: '',
            message: '',
            level:'2',
            trigger: []
        }
    }
    $.extend(this._option, options);
    if (this._option.validRules) {
        for (var i = 0, len = this._option.validRules.length; i < len; i++) {
            var item = this._option.validRules[i];
            if (this._data.valid._map[item.mode]) {
                this._data.valid._map[item.mode].isUse = true;
                this._data.valid._map[item.mode].data = item.data;
                this._data.valid._map[item.mode].message = item.message;
                this._data.valid._map[item.mode].level = item.level||this._data.valid._map[item.mode].level;

            } else {
                this._data.valid._map[item.mode] = {
                    mode: item.mode,
                    isUse: true,
                    status: false,
                    data: item.data,
                    message: item.message,
                    level:0
                }
            }
            if (item.trigger) {
                this._data.valid._map[item.mode].trigger = item.trigger.split(',');
            } else {
                this._data.valid._map[item.mode].trigger.push('blur');
            }
        }
    }
    this._selector = '[data-view="' + this._option.parentName + '"] [data-propertyname="' + this._option.name + '"]'
    this._element = typeof this._option.name == 'string' ? $(this._selector) : this._option.name;
    typeof this.init == 'function' ? this.init() : '';
}
/**
 * 获取是否是输入值的域
 * @returns {string}
 */
lg.Widgets.BaseControl.prototype.getIsValueField = function() {
    return this._isValueField;
}
lg.Widgets.BaseControl.prototype.setIsValueField = function(val) {
    var value = false;
    if (val) {
        value = true;
    }
    this._isValueField = value;
}
/**
 * 获取控件实例名
 * @returns {string}
 */
lg.Widgets.BaseControl.prototype.getName = function() {
    return this._option.name;
}
lg.Widgets.BaseControl.prototype.getElement = function() {
    return this._element;
}
    /**
     * 初始化控件
     * @param options
     */
lg.Widgets.BaseControl.prototype.BaseInit = function(options) {
    this.setData(options); //初始化控件参数
    var that = this;
    var isVisible = true;
    if(!this._option.isFocusShow){
        this.getElement().find('input[type="text"],input[type="password"],input[type="checkbox"],input.btn_outline').on('focus', function(e) {
            that.setValidMessage();
        });
    }
    typeof this._option.isVisible == 'undefined'?isVisible:isVisible=false;
    this.setVisible(isVisible);
    
    //验证触发事件定义    ==> keyup blur
    this.getElement().find('input[type="text"],input[type="password"]').on('blur keydown change keyup', {control: this},function(e) {
        var that = e.data.control;
        if (e.type == 'keydown') {
            that._isDirty = true;
        }
        var value = that.getValue();
        var validResult = that.getIsValid(value, e.type);
        if(that._isDirty&& that.getSelfIsValided()&&(e.type=="keyup"||e.type=="change")){
            
            if(that._option.keyup){
                that.execValid(that.getValue());
                that._option.keyup.call(this, {
                control: that,
                isValidat:true,
                parent: lg.Cache.Views[that._option.parentName],
                linkFor:lg.Cache.Views[that._option.parentName].field[that._option.linkFor]
            })
            }
        }else if(that._isDirty&& !that.getSelfIsValided()&&(e.type=="keyup"||e.type=="change")){
           
            if(that._option.keyup){
                that.execValid(that.getValue());
                that._option.keyup.call(this, {
                control: that,
                isValidat:false,
                parent: lg.Cache.Views[that._option.parentName],
                linkFor:lg.Cache.Views[that._option.parentName].field[that._option.linkFor]
            })
            }
        }
        if (lg.Utils.isNullObject(validResult)) {
            that.setValidMessage(validResult);
            return;
        } else {
            that.setValidMessage();
        }
        
    });
}

lg.Widgets.BaseControl.prototype.showMessage = function(val){
    this.getElement().find('[data-valid-message]').length ? '' : this.getElement().append('<span data-valid-message class="input_tips"></span>');
    var messageBox = this.getElement().find('[data-valid-message]');
    var message = messageBox.html();
    if (lg.Utils.isNullObject(val)) {
        messageBox.empty();
        var messageList = '';
        
        messageBox.html(val.message);
        messageBox.show();
        this.getElement().find('input[type="text"]').addClass('input_warning');
        this.getElement().find('input[type="password"]').addClass('input_warning');
    } else {
        messageBox.remove();
        this.getElement().find('input[type="text"]').removeClass('input_warning');
        this.getElement().find('input[type="password"]').removeClass('input_warning');
    }   
}
lg.Widgets.BaseControl.prototype.setValidMessage = function(val,from) {
        if(this._option.forbidAddMessageBySelf){
            if(from=="CollectData"){
                this.getElement().find('[data-valid-message]').length ?'' : this.getElement().append('<span data-valid-message class="input_tips"></span>');
                var messageBox = this.getElement().find('[data-valid-message]');
            }else{
                var messageBox = this.getElement().find('[data-valid-message]');
                if(!messageBox && messageBox.length>0){
                    return;
                }
            }
            
        }else{
            this.getElement().find('[data-valid-message]').length ?'' : this.getElement().append('<span data-valid-message class="input_tips"></span>');
            var messageBox = this.getElement().find('[data-valid-message]');
        }
        

        var message = messageBox.html();
        if (lg.Utils.isNullObject(val || {})) {
            messageBox.empty();
            var messageList = '';
            var level = 0;
            for (var item in val) {
                typeof val[item].level !='undefined'?(level = (level<val[item].level)?val[item].level:level):'';
            }
            for (var item in val) {
                if(typeof val[item].level !='undefined'&& level == val[item].level){
                    messageList = val[item].message;
                }
            }
            messageBox.html(messageList);
            messageBox.show();
            this.getElement().find('input[type="text"]').addClass('input_warning');
            this.getElement().find('input[type="password"]').addClass('input_warning');
        } else {
            messageBox.remove();
            this.getElement().find('input[type="text"]').removeClass('input_warning');
            this.getElement().find('input[type="password"]').removeClass('input_warning');
        }
    }
    /**
     *设置控件参数
     * @param data
     */
lg.Widgets.BaseControl.prototype.setData = function(data) {
    for (var item in data) {
        this['set' + item] = data[item];
    }
}

    /**
     *初始化
     * @param data
     */
lg.Widgets.BaseControl.prototype.setClear = function() {

    this.getElement().find('input.input_warning').removeClass('input_warning');
    this.getElement().find('[data-valid-message]').remove();
    this.getElement().find('input[type="text"],input[type="password"]').val('');
    this._isDirty = false;
    this.getElement().find('input[type="text"],input[type="password"]').blur();
}

/**
 * 获取控件是否只读
 * @returns {boolean}
 */
lg.Widgets.BaseControl.prototype.getIsReadOnly = function() {
    return this.getElement().attr('readonly') ? true : false;
}

/**
 * 设置控件是否只读
 * @param val
 */
lg.Widgets.BaseControl.prototype.setReadOnly = function(val) {
    var value = false;
    if (val) {
        value = true;
    }
    value ? this.getElement().attr('readonly', value) : this.getElement().removeAttr('readonly');
}

/**
 * 获取控件是否可用
 * @returns {boolean}
 */
lg.Widgets.BaseControl.prototype.getIsDisabled = function() {
    return this.getElement().attr('disabled') ? true : false;
}

/**
 * 设置是否获取焦点
 * @param val
 * @returns {*}
 */
lg.Widgets.BaseControl.prototype.setFocus = function(val) {
        var value = false;
        if (val) {
            value = true;
            this.getElement().find('input[type ="text"]').focus();
        }
        //this.getElement().find('input[text]').focus();
    }
    /**
     * 设置控件是否可用
     * @param val
     */
lg.Widgets.BaseControl.prototype.setDisable = function(val) {
    var value = false;
    if (val) {
        value = true;
    }
    value ? this.getElement().attr('disabled', value) : this.getElement().removeAttr('disabled');
    if(value){
        this.getElement().attr('disabled', value);
        this.getElement().find('input[type="button"]').attr('disabled', value);
    }else{
        this.getElement().removeAttr('disabled');
        this.getElement().find('input[type="button"]').removeAttr('disabled');
    }
}

/**
 * 获取控件是否可见
 * @returns {boolean}
 */
lg.Widgets.BaseControl.prototype.getIsVisible = function() {
    return this.getElement().css('display') != 'none' ? true : false;
}

/**
 * 设置控件是否可见
 * @param val
 */
lg.Widgets.BaseControl.prototype.setVisible = function(val) {
    var value = 'none';
    if (val) {
        value = 'block';
    }
    this.getElement().css('display', value);
}

/**
 * 获取验证结果
 * @returns {Array}
 */
lg.Widgets.BaseControl.prototype.getIsValid = function(val, type) {
    this.execValid(val, type);
    return this._data.valid.validResult;
}

/**
 * 设置控件验证规则
 * @param val
 */
lg.Widgets.BaseControl.prototype.setValid = function(val) {
        for (var item in val) {
            this._data.valid._map[item].is = val[item];
        }
    }
    /**
     * 获取值
     * @param val
     */
lg.Widgets.BaseControl.prototype.getValue = function() {
    this._value = typeof this.getElement().find('input[type="text"]').val() == 'undefined' ? this.getElement().find('input[type="password"]').val() : this.getElement().find('input[type="text"]').val();
    this._value = typeof this._value =='undefined'?'':this._value;
    this._value = this._value.trim();
    return this._value;
}

lg.Widgets.BaseControl.prototype.setValue = function(val) {
        this._value = this.getElement().find('input[type="text"]').val(val) || this.getElement().find('input[type="password"]').val(val);
    }
    /**
     * 执行验证规则
     * @param val
     */
lg.Widgets.BaseControl.prototype.execValid = function(val, type) {
    var thisType = type || 'blur';
    if (typeof val == 'undefined' || !this.getIsVisible()) return;
    for (var item in this._data.valid._map) {
        if (typeof this._data.valid._map[item] == 'object') {
            if (this._data.valid._map[item].isUse) {
                if (this._data.valid._map[item].mode == 'require') {
                    this.controlValidResult((val.length == 0)&&this._isDirty&&(this._data.valid._map[item].trigger.indexOf(thisType) > -1), item,type);
                }
                if (this._data.valid._map[item].mode == 'min-len') {
                    this.controlValidResult((val.length < this._data.valid._map[item].data) && this._isDirty && (this._data.valid._map[item].trigger.indexOf(thisType) > -1), item,type);
                }
                if (this._data.valid._map[item].mode == 'max-len') {
                    this.controlValidResult((val.length > this._data.valid._map[item].data) && this._isDirty && (this._data.valid._map[item].trigger.indexOf(thisType) > -1), item,type);
                }
                if (this._data.valid._map[item].mode == 'repeat-password') {
                    var pwd = lg.Cache.Views[this._option.parentName].field[this._option.linkFor].getValue();
                    var repwd = this.getValue();
                    this.controlValidResult((pwd != repwd) && this._isDirty && (this._data.valid._map[item].trigger.indexOf(thisType) > -1), item ,type);
                }
                if (this._data.valid._map[item].mode == 'pattern') {
                   
                    if(typeof this._data.valid._map[item].data=='string'){
                        var data = this._data.valid._map[item].data.split('||');
                        var temp = false;
                        for(var i=0,len=data.length;i<len;i++){
                            var reg = eval(data[i]);
                            temp = temp || reg.test(val);    
                        }         
                    }else{
                        var data = this._data.valid._map[item].data;
                        var temp = false;
                         for(var i in data){
                            if(typeof data[i] !='function'){
                                temp = temp || data[i].test(val);
                            }
                        }   
                    }
                        this.controlValidResult((!temp) && this._isDirty && (this._data.valid._map[item].trigger.indexOf(thisType) > -1), item,type);
                }
            }
        }

    }
}
lg.Widgets.BaseControl.prototype.getSelfIsValided = function() {
    var value = true;
    var val = this.getValue();
    if (typeof val == 'undefined') return false;
    for (var item in this._data.valid._map) {
        if (typeof this._data.valid._map[item] == 'object') {
            if (this._data.valid._map[item].isUse) {
                if (this._data.valid._map[item].mode == 'require') {
                     value && (val.length != 0)?value=true:value=false;
                }
                if (this._data.valid._map[item].mode == 'min-len') {
                     value && (val.length > this._data.valid._map[item].data)?value=true:value=false;
                }
                if (this._data.valid._map[item].mode == 'max-len') {
                    value && (val.length < this._data.valid._map[item].data)?value=true:value=false;
                }
                if (this._data.valid._map[item].mode == 'repeat-password') {
                    var pwd = lg.Cache.Views[this._option.parentName].field[this._option.linkFor].getValue();
                    var repwd = this.getValue();
                    value && (pwd == repwd)?value=true:value=false;
                }
                if (this._data.valid._map[item].mode == 'pattern') {
                    if(typeof this._data.valid._map[item].data=='string'){
                        var data = this._data.valid._map[item].data.split('||');
                        var temp = false;
                        for(var i=0,len=data.length;i<len;i++){
                            var reg = eval(data[i]);
                            temp = temp || reg.test(val);    
                        }         
                    }else{
                        var data = this._data.valid._map[item].data;
                        var temp = false;
                         for(var i in data){
                            if(typeof data[i] !='function'){
                                temp = temp || data[i].test(val);
                            }
                        }   
                    }
                    value && temp ? value=true:value=false;
                   
                }
            }
        }

    }
    return value;
}
lg.Widgets.BaseControl.prototype.controlValidResult = function(val, item , type) {
    //var result = type ==""
    if(!!val){
        this._data.valid.validResult[this._data.valid._map[item].mode] = this._data.valid._map[item];
        this._data.valid.validResult[this._data.valid._map[item].mode].triggerType = type;
    }else{
        delete this._data.valid.validResult[this._data.valid._map[item].mode]
    }
}
lg.Widgets.Controls = {};
lg.Widgets.Controls.Phone = function(controlType, func) {
    lg.Widgets.Controls[controlType] = func(controlType);
};

lg.Widgets.Controls.Extend = function(controlType, func) {
    lg.Widgets.Controls[controlType] = func(controlType);
};

lg.Widgets.Controls.Extend("Phone", function(controlType) {
    var _shieldChar;
    var control = function(id, options) {
        lg.Widgets.BaseControl.call(this, id, options);
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;
    return control;
});

lg.Widgets.Controls.Extend("PhoneVerificationCode", function(controlType) {
    var _shieldChar;
    var control = function(id, options) {
        lg.Widgets.BaseControl.call(this, id, options);
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;

    /**
     * 获取设置的时长
     * @returns {number|*}
     */
    control.prototype.getTopTime = function() {
        return this._option.topTime || 60;
    }

    /**
     * 设置总时长
     * @param val
     */
    control.prototype.setTopTime = function(val) {
        this._option.topTime = val;
    }

    /**
     *获取验证码获取总次数
     * @returns {*}
     */
    control.prototype.getopCount = function() {
        return this._option.topCount || null;
    }
    control.prototype.getTotalCount = function(val) {
        return this._option.totalCount;
    }
    control.prototype.setTotalTimeTemp = function() {
        this.totalTimeTemp = this.getTopTime();
    }
    control.prototype.setTimeLine = function(val) {
        this._option.timeLine = val;
    }
    control.prototype.getPhoneVerificationCodeUrl = function() {
        return this._option.url;
    }
    control.prototype.getVerificationButton = function() {
        return this.getElement().find('input[type="button"]');
    }

    control.prototype.getVerificationInput = function() {
        return this.getElement().find('input[type="text"]');
    }
    control.prototype.getCodeIsDisabled = function() {
        return this.getElement().find('input[type="button"]').hasClass('btn_disabled');
    }
    control.prototype.setCodeIsDisabled = function(val) {
        var value = false;
        if(val){
            value = true;
            this.getElement().find('input[type="button"]').addClass('btn_disabled');
            return value;
        }else{
            this.getElement().find('input[type="button"]').removeClass('btn_disabled');
            return value;
        }
        
    }
    control.prototype.getLinkFor = function() {
        return lg.Cache.Views[this._option.parentName].field[this._option.linkFor];
    }
    control.prototype.init = function() {
        //this.count = this.getTotalCount();
        this.timeLine = null;
        this.isActive = false;
        //var that = this;
        //if(this._option.codeIsDisabled){
        this.setCodeIsDisabled(this._option.codeIsDisabled);
        //}
        
        var linkFor = lg.Cache.Views[this._option.parentName].field[this._option.linkFor];

        if(!linkFor.getSelfIsValided()&&linkFor._option.keyup){
            this.getVerificationButton().val((typeof this._option.postfix!='string')?'获取验证码':'获取');
            
        }else if(linkFor.getSelfIsValided()&&linkFor._option.keyup){
            this.getVerificationButton().removeClass('btn_disabled').val((typeof this._option.postfix!='string')?'获取验证码':'获取');
        }
        this.totalTimeTemp = this.getTopTime();
        this.getElement().find('input[type="button"]').one('click', {
            control: this
        }, function(e) {
            var that = e.data.control; 
            var isValidateLinkAndVerifyCode = true;
            var linkFor = lg.Cache.Views[that._option.parentName].field[that._option.linkFor];
            var verifyCode = lg.Cache.Views[that._option.parentName].field[that._option.verifyCode];
            if(verifyCode.getIsVisible()){
                verifyCode.getSelfIsValided()&&isValidateLinkAndVerifyCode?isValidateLinkAndVerifyCode=true:isValidateLinkAndVerifyCode=false;
            }
            linkFor.getSelfIsValided()&&isValidateLinkAndVerifyCode?isValidateLinkAndVerifyCode=true:isValidateLinkAndVerifyCode=false;
            if(isValidateLinkAndVerifyCode){
                that.setDisable(true);
                if(!that.getCodeIsDisabled()&& that.getIsDisabled()){
                        that.isActive = true;
                        that._option.click.call(this, {
                            control: that,
                            parent: lg.Cache.Views[that._option.parentName],
                            linkFor:linkFor
                        })
                   
                    
                }
            }else{

                linkFor._isDirty=true;
                linkFor.setValidMessage(linkFor.getIsValid(linkFor.getValue()),'CollectData');
                if(verifyCode.getIsVisible()){
                    verifyCode._isDirty=true;
                    verifyCode.setValidMessage(verifyCode.getIsValid(verifyCode.getValue()),'CollectData');
                }
                that.init();
            }
           
            //e.data.control.starttime(e.data.control);
        });
    }
    control.prototype.getVerificationCode = function(){

    }
    control.prototype.setClear = function() {

        this.getElement().find('input.input_warning').removeClass('input_warning');
        this.getElement().find('[data-valid-message]').remove();
        this.getElement().find('input[type="text"],input[type="password"]').val('');
        this._isDirty = false;
        this.getElement().find('input[type="text"],input[type="password"]').blur();
        clearInterval(this.timeLine);
        
        var objEvt = $._data(this.getElement().find('input[type="button"]')[0], "events");
        if (objEvt && objEvt["click"]) {
            //console.info(objEvt["click"]);
            //alert("bind click");
        }
        else {
            this.init();
        }
        this.timeLine = null;
        this.setDisable(false);
        var linkFor = lg.Cache.Views[this._option.parentName].field[this._option.linkFor];
        if(!linkFor.getSelfIsValided()&&linkFor._option.keyup){
            //this.init();
            this.getVerificationButton().val((typeof this._option.postfix!='string')?'获取验证码':'获取');
            
        }else{
            //this.init();

            this.getVerificationButton().removeClass('btn_disabled').val((typeof this._option.postfix!='string')?'获取验证码':'获取');
            
        }
    }
    control.prototype.starttime = function(that) {
        if (!that.timeLine) {
            that.totalTimeTemp = that.getTopTime();
            
            that.timeLine = setInterval(function() {
                var self = lg.Cache.Views[that._option.parentName].field[that.getName()];
                self.totalTimeTemp--;
                var text = (typeof self._option.postfix!='string')?'秒后重试':self._option.postfix+'s';
                self.getVerificationButton().addClass('btn_disabled').val(self.totalTimeTemp + text);
                if (self.totalTimeTemp == -1) {
                    clearInterval(self.timeLine);
                    self.timeLine = null;
                    that.setDisable(false);
                    var linkFor = lg.Cache.Views[that._option.parentName].field[that._option.linkFor];
                    if(!linkFor.getSelfIsValided()&&linkFor._option.keyup){
                        self.init();
                        self.getVerificationButton().val((typeof self._option.postfix!='string')?'获取验证码':'获取');
                        
                    }else{

                        self.init();
                        self.getVerificationButton().removeClass('btn_disabled').val((typeof self._option.postfix!='string')?'获取验证码':'获取');
                    }
                    //self.getVerificationButton().removeClass('btn_disabled').val((typeof self._option.postfix!='string')?'获取验证码':'获取');
                   // self.getVerificationButton().
                    //self.count--;
                }
            }, 1000);
        } 
        /*else if (that.count == 0) {
            console.log(that);
            //window.localStorage.getItem('')
            that.showMessage({message:that._option.totalTips||"已经达到限定次数"})
        }*/
    }
    return control;
});

lg.Widgets.Controls.Extend("Password", function(controlType) {
    var _shieldChar;
    var control = function(options) {
        lg.Widgets.BaseControl.call(this, options);
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;
    return control;
});

lg.Widgets.Controls.Extend("RepeatPassword", function(controlType) {
    var _shieldChar;
    var control = function(options) {
        lg.Widgets.BaseControl.call(this, options);
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;
    return control;
});

lg.Widgets.Controls.Extend("Email", function(controlType) {
    var _shieldChar;
    var control = function(options) {
        lg.Widgets.BaseControl.call(this, options);
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;
    return control;
});


lg.Widgets.Controls.Extend("VerifyCode", function(controlType) {
    var _shieldChar;
    var control = function(options) {
        lg.Widgets.BaseControl.call(this, options);
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;
    control.prototype.init = function() {
        //ar url = this.getVerifyCodeUrl();
        //this.getVerifyCodeImg().attr("src", url);
        this.getVerifyCodeReflashButton().on('click', {
            control: this
        }, function(e) {

            var url = e.data.control.getVerifyCodeUrl();
            var img = $('<img class="yzm" />');
            if(e.data.type=='init'){
                if(e.data.control.getVerifyCodeImg().attr("src")){
                    return;
                }else{
                    img.attr('src',url);
                    $('[data-controltype="VerifyCode"]').find('img').remove();
                    $('[data-controltype="VerifyCode"]').find('input').after(img);
                }//?'':img.attr('src',url);
            }else{          
                img.attr('src',url);
                $('[data-controltype="VerifyCode"]').find('img').remove();
                $('[data-controltype="VerifyCode"]').find('input').after(img);
            }
            
            //e.data.control.getVerifyCodeImg().attr("src", url);
        });
    }
    control.prototype.getVerifyCode = function() {
        this.getVerifyCodeReflashButton().trigger('click',{
            control: this,
            type:'init'
        });
    }
    control.prototype.getFrom = function() {
        return this._option.from || 'register';
    }
    control.prototype.getVerifyCodeUrl = function() {
        var url = this._option.url + '?from=' + this.getFrom() + '&refresh=' + new Date().getTime();
        return url;
    }
    control.prototype.getVerifyCodeReflashButton = function() {
        return this.getElement().find('a');
    }
    control.prototype.getVerifyCodeInput = function() {
        return this.getElement().find('input');
    }
    control.prototype.getVerifyCodeImg = function() {
        return this.getElement().find('img');
    }
    return control;
});


lg.Widgets.Controls.Extend("Switch", function(controlType) {
    var _shieldChar;
    var control = function(options) {
        lg.Widgets.BaseControl.call(this, options);
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;
    control.prototype.getValue = function() {
    return this.getElement().find('.btn_active').attr('data-myvalue')||'';
    }
    
    return control;
});
lg.Widgets.Controls.Extend("CheckBox", function(controlType) {
    var _shieldChar;
    var control = function(options) {
        lg.Widgets.BaseControl.call(this, options);
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;
    control.prototype.getValue = function() {
        var chk_value = [];
        this.getElement().find('input[type="checkbox"]:checked').each(function() {
            chk_value.push($(this).attr("data-myvalue"));
        });
        return chk_value;
    }
    return control;
});
lg.Widgets.Controls.Extend("Button", function(controlType) {
    var _shieldChar;
    var control = function(options) {
        lg.Widgets.BaseControl.call(this, options);
        this._isValueField = false;
    };
    control.prototype = new lg.Widgets.BaseControl();
    control.prototype.controlType = controlType;
    control.prototype.init = function() {
        this.isActive = false;
        this.getElement().find('[type="button"]').on('click', {
            control: this
        }, function(e) {
            var that = e.data.control;
            that.isActive = true;
            that._option.click.call(this, {
                    control: that,
                    parent: lg.Cache.Views[that._option.parentName]
                })

                //console.log(lg.Cache.Views[that._option.parentName].CollectData());
        });
    }
    return control;
});
//------------------------------------------------------------------  end




/**-----------------------------------------------------------------  start
 * 命名控件 - 视图
 */

lg.Views = lg.Views || {};

lg.Views.BaseView = function(options) {
    this._name = '';
    this._children = [];
    this._Validation = {};
    this._options = {};
    this.childrenData = {};
    this.field = {};
    if (options) {
        this._name = options.name;
    }
    $.extend(this._options, options);
    this._element = typeof options.name == 'string' ? $('[data-view="' + this._name + '"]') : this._name;
    lg.Cache.Views[this._name] = this;
    this.init();
}
lg.Views.BaseView.prototype.getElement = function() {
    return this._element;
}
lg.Views.BaseView.prototype.setClear = function(){
    for (var item in this.field) {
        this.field[item].setClear();
    }
}
lg.Views.BaseView.prototype.ValidatForm = function() {

    for (var item in this.field) {
        var temp = {};
        var i = {};
        if(this.field[item].getIsValueField()){
            this.field[item]._isDirty=true;
            i = this.field[item].getIsValid(this.field[item].getValue());
        }
        if (lg.Utils.isNullObject(i)) {
            this._Validation[item] = i;
        } else {
            delete this._Validation[item];
        }
        //?(delete this._Validation[item]):this._Validation[item]=i;

    }
    if (lg.Utils.isNullObject(this._Validation)) {
        for (var item in this._Validation) {
            this.field[item].setValidMessage(this._Validation[item],'CollectData')
        }
        return false;
    }
    return true;
}
lg.Views.BaseView.prototype.CollectData = function(val) {
    this.childrenData.isValidate = true;
    if(!val){
         this.childrenData.isValidate = this.ValidatForm();
    }
    
    for (var item in this.field) {
        if(this.field[item].getIsValueField()){
            this.childrenData[item] = this.field[item] ? this.field[item].getValue() : '';
        }
    }
    return this.childrenData;
}
lg.Views.BaseView.prototype.init = function() {
    this._options;
    this._options.fields ? this.initControls(this._options.fields) : '';
}
lg.Views.BaseView.prototype.initControls = function(fields) {
    for (var i = 0, len = fields.length; i < len; i++) {
        fields[i].parentName = this._name;
        this.field[fields[i].name] = new lg.Widgets.Controls[fields[i].controlType](fields[i]);
        this.field[fields[i].name].BaseInit()
            //typeof this.field[fields[i].name].init == "function"?this.field[fields[i].name].init():'';
    }
}
lg.Views.BaseView.prototype.extend = function(name, func) {
    this[name] = func;
}

//------------------------------------------------------------------  end





/**-----------------------------------------------------------------  start
 * 命名控件 - 模型
 */

lg.Models = lg.Models || {};

lg.Models.BaseViewModel = function(viewName, options) {
    if (viewName) {
        this._name = viewName;
    }
    this._name = '';
    $.extend(this._options, options);
}



//------------------------------------------------------------------  end