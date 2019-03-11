/*!mobile/modules/country-code/main.js*/
;define("mobile/modules/country-code/main",["require","exports","module"],function(){var c=0,a=0,_=1,g=$(".area_code_list"),h=$(".area_code");$.ajax({url:"/register/getPhoneCountryCode.json",success:function(y){var L,i,k,v,b="",j=y.content.rows,w=j[c].countryList[c].code;if(h.text(w).data("default-code",w),y.state===_&&j)for(L=c,k=j.length;k>L;L++)for(b+="<dt>"+j[L].name+"</dt>",i=c,v=j[L].countryList.length;v>i;i++)b+='<dd data-code="'+j[L].countryList[i].code+'">'+j[L].countryList[i].name+"</dd>";else b="请求出错";$(".code_list_main").append(b),$(".area_code").on("click",function(){return g.is(":visible")?g.hide():g.show().scrollTop(a),!1}),$(".area_code_list dd").on("click",function(){return h.text($(this).data("code")),$(".area_code").trigger("click"),!1})}})});
/*!mobile/common/widgets/validator/main.js*/
;define("mobile/common/widgets/validator/main",["require","exports","module"],function(require,exports,module){function F(F){this.phoneInputSelector=F.phoneInputSelector,this.emailInputSelector=F.emailInputSelector,this.userInputSelector=F.userInputSelector,this.passwordInputSelector=F.passwordInputSelector,this.vcodeInputSelector=F.vcodeInputSelector,this.pcodeInputSelector=F.pcodeInputSelector}F.prototype={constructor:F,validatePhone:function(F){var c,a=$(this.phoneInputSelector).val().trim();if(a){if(/^\d{5,11}$/.test(a))return"function"==typeof F&&F(null),!0;c="手机格式不正确，请重新输入"}else c="请输入手机号码";return"function"==typeof F&&F({"class":this.phoneInputSelector,message:c}),!1},validateVcode:function(F){var c,a=$(this.vcodeInputSelector).val().trim();if(a){if(/^[0-9]{6,6}$/.test(a))return"function"==typeof F&&F(null),!0;c="请输入正确的手机验证码"}else c="请输入手机验证码";return"function"==typeof F&&F({"class":this.vcodeInputSelector,message:c}),!1},validatePcode:function(F){if(0===$(this.pcodeInputSelector).length)return"function"==typeof F&&F(null),!0;var c,a=$(this.pcodeInputSelector).val().trim();if(a){if(/^[a-zA-Z0-9\u4e00-\u9fa5]{4,4}$/.test(a))return"function"==typeof F&&F(null),!0;c="请输入正确的图形验证码"}else c="请输入图形验证码";return"function"==typeof F&&F({"class":this.pcodeInputSelector,message:c}),!1},validateEmail:function(F){var c,a=$(this.emailInputSelector).val().trim();if(a){if(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))$/i.test(a))return"function"==typeof F&&F(null),!0;c="请输入有效的邮箱"}else c="请输入邮箱";return"function"==typeof F&&F({"class":this.emailInputSelector,message:c}),!1},validateUser:function(F){var c,a=$(this.userInputSelector).val().trim();if(a){if(/^\d{5,15}$/.test(a)||this.validateEmail())return"function"==typeof F&&F(null),!0;c="请输入有效的手机/邮箱"}else c="请输入已验证手机/邮箱";return"function"==typeof F&&F({"class":this.userInputSelector,message:c}),!1},validatePassword:function(F){var c,a=$(this.passwordInputSelector).val().trim();if(a){if(/^\S{6,16}$/.test(a))return"function"==typeof F&&F(null),!0;c="请输入6-16位密码，字母区分大小写"}else c="请输入密码";return"function"==typeof F&&F({"class":this.passwordInputSelector,message:c}),!1}},module.exports=F});
/*!mobile/page/register-land/main.js*/
;define("mobile/page/register-land/main",["require","exports","module","mobile/modules/country-code/main","mobile/common/widgets/validator/main"],function(require){function a(){S&&initSense({id:"66442f2f720bfc86799932d8ad2eb6c7",https:!0,onError:function(a){console.log("gt error",a)}},function(a){a._c_interactive=0,a.setInfos(function(){return{interactive:a._c_interactive}}).onSuccess(function(c){a._c_onSuccess&&a._c_onSuccess(c)}).onClose(function(){a.reset()}).onError(function(){window.location.reload()}),C=a})}function c(){$(P).attr("src","https://passport.lagou.com/vcode/create?from=register&refresh="+Date.now())}function g(a,g){clearTimeout(G),$("#popLayer").remove(),g&&$(g).addClass("error"),$("body").append('<div id="popLayer">'+a+"</div>"),$("#popLayer").addClass("pop"),g===z&&c(),G=setTimeout(function(){$("#popLayer").remove()},H)}function v(){var a=null,c=60,g=0;$(L).val(c+"s").addClass("btn_disabled"),clearInterval(a),a=setInterval(function(){return c--,g>c?(clearInterval(a),void $(L).val($(L).attr("placeholder")).removeClass("btn_disabled")):void $(L).val(c+"s")},I)}function b(){if(S){if(!C)return;C._c_interactive=3,C._c_onSuccess=function(a){_(a.challenge)},C.sense()}else _()}function _(a){var b=$(E).val().trim(),_=$.trim($(z).val()),y=$(V).text();$.ajax({url:"/register/getPhoneVerificationCode.json",data:{countryCode:y,phone:b,type:0,request_form_verifyCode:_,challenge:a},dataType:"json",cache:!1,success:function(a){if(a.state===j)return void v();var b=A[a.state];b?g(b.message,b.labelfor):g(a.message),a.state===k&&c()},error:function(){g("系统错误")}})}function y(a){var c=!0;return F.validatePhone(function(g){g?(c=!1,"function"==typeof a&&a(g)):F.validatePcode(function(g){g?(c=!1,"function"==typeof a&&a(g)):F.validateVcode(function(g){g?(c=!1,"function"==typeof a&&a(g)):"function"==typeof a&&a(null)})})}),c}function h(a){var v=$(E).val().trim(),b=$.trim($(D).val()),_=$.trim($(z).val()),y=$(V).text();S&&(a=111),$.ajax({url:"/register/register.json",data:{countryCode:y,type:0,phone:v,phoneVerificationCode:b,request_form_verifyCode:_,source:"lagou_mobile",challenge:a},type:"post",dataType:"json",cache:!1}).done(function(a){if(a.state===j){var v="/grantServiceTicket/grant.html";return void(window.location.href=v)}a.state===k&&c();var b=B[a.state];b?g(b.message,b.labelfor):g(a.message)})}require("mobile/modules/country-code/main");var C,S="nolagou"===$.trim($("#verifyStyle").val()),w=require("mobile/common/widgets/validator/main"),I=1e3,j=1,k=10010,P=".pcode_img",T=".pcode_link",L=".vcode_link",V=".area_code",E=".phone_input",D=".vcode_input",z=".pcode_input:visible",A={1:{message:"验证码已发送，请查收短信",labelfor:D},201:{message:"请输入手机号码",labelfor:E},203:{message:"输入号码与归属地不匹配",labelfor:E},204:{message:"系统错误"},205:{message:"输入号码与归属地不匹配",labelfor:E},206:{message:"系统错误"},208:{message:"验证码发送太过频繁，请稍后再试",labelfor:D},209:{message:"该手机已被注册，请重新输入或直接登录",labelfor:E},220:{message:"手机格式不正确，请重新输入",labelfor:E},222:{message:"该手机号未注册"},310:{message:"验证码达到发送上限（5次），无法继续发送",labelfor:D},311:{message:"操作太过频繁，请稍后再试"},402:{message:"手机验证码不正确",labelfor:D},10010:{message:"图形验证码不正确",labelfor:z},10011:{message:"操作过于频繁，请联系管理员"},10012:{message:"操作过于频繁，请联系管理员"}},B={1:{message:"成功"},203:{message:"输入号码与归属地不匹配",labelfor:E},209:{message:"该手机已被注册，请重新输入或直接登录",labelfor:E},222:{message:"输入号码与归属地不匹配",labelfor:E},240:{message:"请输入手机号码",labelfor:E},245:{message:"请输入6位数字验证码",labelfor:D},401:{message:"手机验证码不正确",labelfor:D},402:{message:"手机验证码不正确",labelfor:D},403:{message:"系统错误"},500:{message:"系统错误"},501:{message:"系统错误"},502:{message:"系统错误"},10010:{message:"图形验证码不正确",labelfor:z},10011:{message:"操作过于频繁，请联系管理员"},10012:{message:"操作过于频繁，请联系管理员"}},F=new w({phoneInputSelector:E,vcodeInputSelector:D,pcodeInputSelector:z});a();var G=null,H=2e3;$(T).on("click",c),$(L).on("click",function(){$(this).hasClass("btn_disabled")||F.validatePhone(function(a){a?g(a.message,a.class):F.validatePcode(function(a){a?g(a.message,a.class):b()})})}),$(".form_register").on("submit",function(){return y(function(a){a?g(a.message,a.class):h()}),!1}),$('input[type="text"]').on("focus",function(){$(this).removeClass("error")})});