(function(e){function t(t){for(var r,c,u=t[0],s=t[1],i=t[2],l=0,f=[];l<u.length;l++)c=u[l],Object.prototype.hasOwnProperty.call(o,c)&&o[c]&&f.push(o[c][0]),o[c]=0;for(r in s)Object.prototype.hasOwnProperty.call(s,r)&&(e[r]=s[r]);d&&d(t);while(f.length)f.shift()();return a.push.apply(a,i||[]),n()}function n(){for(var e,t=0;t<a.length;t++){for(var n=a[t],r=!0,c=1;c<n.length;c++){var u=n[c];0!==o[u]&&(r=!1)}r&&(a.splice(t--,1),e=s(s.s=n[0]))}return e}var r={},c={app:0},o={app:0},a=[];function u(e){return s.p+"static/js/"+({about:"about"}[e]||e)+"-legacy."+{about:"c5dd133a","chunk-2068c20c":"6ec3523b","chunk-34a62f8b":"2e592962","chunk-4008f205":"b7531f1b","chunk-4eb36d89":"3aa74b43","chunk-5928e08c":"9474d16b","chunk-68f67dc5":"ab3966b8","chunk-82e985f2":"395fe0b0"}[e]+".js"}function s(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.e=function(e){var t=[],n={about:1,"chunk-2068c20c":1,"chunk-34a62f8b":1,"chunk-4008f205":1,"chunk-4eb36d89":1,"chunk-5928e08c":1,"chunk-68f67dc5":1,"chunk-82e985f2":1};c[e]?t.push(c[e]):0!==c[e]&&n[e]&&t.push(c[e]=new Promise((function(t,n){for(var r="static/css/"+({about:"about"}[e]||e)+"."+{about:"a5c34beb","chunk-2068c20c":"d0e96263","chunk-34a62f8b":"ebc9fd2a","chunk-4008f205":"35d026c5","chunk-4eb36d89":"f87e398a","chunk-5928e08c":"6e5d9fc9","chunk-68f67dc5":"ec04eb93","chunk-82e985f2":"21d8067a"}[e]+".css",o=s.p+r,a=document.getElementsByTagName("link"),u=0;u<a.length;u++){var i=a[u],l=i.getAttribute("data-href")||i.getAttribute("href");if("stylesheet"===i.rel&&(l===r||l===o))return t()}var f=document.getElementsByTagName("style");for(u=0;u<f.length;u++){i=f[u],l=i.getAttribute("data-href");if(l===r||l===o)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var r=t&&t.target&&t.target.src||o,a=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");a.code="CSS_CHUNK_LOAD_FAILED",a.request=r,delete c[e],d.parentNode.removeChild(d),n(a)},d.href=o;var p=document.getElementsByTagName("head")[0];p.appendChild(d)})).then((function(){c[e]=0})));var r=o[e];if(0!==r)if(r)t.push(r[2]);else{var a=new Promise((function(t,n){r=o[e]=[t,n]}));t.push(r[2]=a);var i,l=document.createElement("script");l.charset="utf-8",l.timeout=120,s.nc&&l.setAttribute("nonce",s.nc),l.src=u(e);var f=new Error;i=function(t){l.onerror=l.onload=null,clearTimeout(d);var n=o[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),c=t&&t.target&&t.target.src;f.message="Loading chunk "+e+" failed.\n("+r+": "+c+")",f.name="ChunkLoadError",f.type=r,f.request=c,n[1](f)}o[e]=void 0}};var d=setTimeout((function(){i({type:"timeout",target:l})}),12e4);l.onerror=l.onload=i,document.head.appendChild(l)}return Promise.all(t)},s.m=e,s.c=r,s.d=function(e,t,n){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)s.d(n,r,function(t){return e[t]}.bind(null,r));return n},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/",s.oe=function(e){throw console.error(e),e};var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var f=0;f<i.length;f++)t(i[f]);var d=l;a.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("cd49")},"0594":function(e,t,n){},"2ce4":function(e,t,n){},4744:function(e,t,n){"use strict";n("0594")},"52ba":function(e,t,n){},"690e":function(e,t,n){},afbc:function(e,t,n){"use strict";n("d3b7");var r=n("6c02"),c=n("7a23"),o=Object(c["withScopeId"])("data-v-326b735c");Object(c["pushScopeId"])("data-v-326b735c");var a=Object(c["createVNode"])("h1",{class:"title"},"科研管理系统",-1),u=Object(c["createVNode"])("h2",null,null,-1),s={id:"loginarea"},i=Object(c["createVNode"])("h1",{class:"logintitle"},"用户登录",-1),l=Object(c["createVNode"])("i",{class:"iconfont icon-bussiness-man"},null,-1),f=Object(c["createVNode"])("i",{class:"iconfont icon-password"},null,-1),d=Object(c["createTextVNode"])("忘记密码"),p=Object(c["createTextVNode"])("登录");Object(c["popScopeId"])();var b=o((function(e,t,n,r,b,h){var m=Object(c["resolveComponent"])("el-header"),g=Object(c["resolveComponent"])("el-col"),j=Object(c["resolveComponent"])("el-row"),O=Object(c["resolveComponent"])("el-input"),k=Object(c["resolveComponent"])("el-link"),v=Object(c["resolveComponent"])("el-button"),w=Object(c["resolveComponent"])("el-main"),y=Object(c["resolveComponent"])("el-container");return Object(c["openBlock"])(),Object(c["createBlock"])(y,null,{default:o((function(){return[Object(c["createVNode"])(m,null,{default:o((function(){return[a,u]})),_:1}),Object(c["createVNode"])(w,null,{default:o((function(){return[Object(c["createVNode"])(j,{class:"loginrow",type:"flex",justify:"center"},{default:o((function(){return[Object(c["createVNode"])(g,{span:6,offset:15,xs:{span:20,offset:2},class:"logincol"},{default:o((function(){return[Object(c["createVNode"])("div",s,[Object(c["createVNode"])(j,null,{default:o((function(){return[Object(c["createVNode"])(g,{span:24},{default:o((function(){return[i]})),_:1})]})),_:1}),Object(c["createVNode"])(j,null,{default:o((function(){return[Object(c["createVNode"])(g,{span:18,offset:3,class:"inputarea"},{default:o((function(){return[Object(c["createVNode"])(O,{placeholder:"请输入账号",modelValue:e.usernum,"onUpdate:modelValue":t[1]||(t[1]=function(t){return e.usernum=t}),clearable:"",onInput:t[2]||(t[2]=function(t){return e.setUserName(e.usernum)}),class:"logininput"},{prepend:o((function(){return[l]})),_:1},8,["modelValue"])]})),_:1})]})),_:1}),Object(c["createVNode"])(j,null,{default:o((function(){return[Object(c["createVNode"])(g,{span:18,offset:3,class:"inputarea"},{default:o((function(){return[Object(c["createVNode"])(O,{placeholder:"请输入密码",modelValue:e.password,"onUpdate:modelValue":t[3]||(t[3]=function(t){return e.password=t}),"show-password":"",onInput:t[4]||(t[4]=function(t){return e.setPassWord(e.password)}),class:"logininput"},{prepend:o((function(){return[f]})),_:1},8,["modelValue"])]})),_:1})]})),_:1}),Object(c["createVNode"])(j,{type:"flex",justify:"center",class:"forgetpassword"},{default:o((function(){return[Object(c["createVNode"])(g,{span:4,offset:16},{default:o((function(){return[Object(c["createVNode"])(k,{type:"primary",disabled:""},{default:o((function(){return[d]})),_:1})]})),_:1})]})),_:1}),Object(c["createVNode"])(j,{type:"flex",justify:"space-around",class:"loginbutton"},{default:o((function(){return[Object(c["createVNode"])(g,{span:12},{default:o((function(){return[Object(c["createVNode"])(v,{onClick:t[5]||(t[5]=function(t){return e.postLogin()})},{default:o((function(){return[p]})),_:1})]})),_:1})]})),_:1})])]})),_:1})]})),_:1})]})),_:1})]})),_:1})})),h=(n("96cf"),n("1da1")),m=n("5502"),g=n("3fd4"),j=n("bc3a"),O=n.n(j),k=n("ad8b"),v=Object(c["defineComponent"])({name:"Login",setup:function(){var e=Object(m["c"])(),t=Object(k["a"])(),n=Object(c["ref"])(""),r=Object(c["ref"])("");Object(c["onMounted"])((function(){t.get("user")&&(e.commit("setUserName",t.get("user")["user"]),e.commit("setLogin",!0),e.commit("setPassWord","cookieLogin"),V.push("/User/first"))}));var o=function(){var n=Object(h["a"])(regeneratorRuntime.mark((function n(){var r,c;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return t.set("user",e.state.username),r=g["a"].service({lock:!1,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"}),n.prev=2,n.next=5,O()({method:"post",url:e.state.loginApi,data:{username:e.state.username,password:e.state.password}});case 5:if(c=n.sent,"2"!=c.data["result"]){n.next=11;break}return r.close(),n.abrupt("return",Object(g["b"])("用户名或密码错误"));case 11:"1"==c.data["result"]&&(e.commit("setLogin",!0),r.close(),t.set("user",{user:e.state.username},{maxAge:86400}),V.push("/User/first"));case 12:n.next=18;break;case 14:return n.prev=14,n.t0=n["catch"](2),r.close(),n.abrupt("return",Object(g["b"])("哎呀，网络似乎有问题呢"));case 18:return n.abrupt("return",null);case 19:case"end":return n.stop()}}),n,null,[[2,14]])})));return function(){return n.apply(this,arguments)}}();return{usernum:n,password:r,postLogin:o}},methods:Object(m["b"])(["setUserName","setPassWord","setLogin"])});n("c1cb");v.render=b,v.__scopeId="data-v-326b735c";var w=v,y=[{path:"/",name:"Login",component:w},{path:"/User",name:"User",component:function(){return n.e("about").then(n.bind(null,"2cbc"))},children:[{path:"first",component:function(){return n.e("chunk-2068c20c").then(n.bind(null,"baa9"))}},{path:"wait",component:function(){return n.e("chunk-4008f205").then(n.bind(null,"9308"))}},{path:"tread",component:function(){return n.e("chunk-68f67dc5").then(n.bind(null,"792d"))}},{path:"paper",component:function(){return n.e("chunk-34a62f8b").then(n.bind(null,"052d"))}},{path:"myPaper",component:function(){return n.e("chunk-4eb36d89").then(n.bind(null,"f21c"))}},{path:"test",component:function(){return n.e("chunk-82e985f2").then(n.bind(null,"5820"))}},{path:"usermanage",component:function(){return n.e("chunk-5928e08c").then(n.bind(null,"867c"))}}]}],N=Object(r["a"])({history:Object(r["b"])(),routes:y}),V=t["a"]=N},c1cb:function(e,t,n){"use strict";n("2ce4")},cd49:function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("7a23");function c(e,t,n,c,o,a){var u=Object(r["resolveComponent"])("router-view");return Object(r["openBlock"])(),Object(r["createBlock"])(u)}var o={name:"App"},a=o;n("4744"),n("e80d");a.render=c;var u=a,s=n("afbc"),i=n("5502"),l=Object(i["a"])({state:{username:"noname",password:"nopassword",islogin:!1,loginApi:"https://www.fastmock.site/mock/0fdbe709330c1a68f26cbef61c777772/graduateSign/loginTest",researchTreadApi:"https://www.fastmock.site/mock/0fdbe709330c1a68f26cbef61c777772/graduateSign/api/tread",newlyResearchApi:"https://www.fastmock.site/mock/0fdbe709330c1a68f26cbef61c777772/graduateSign/api/newlyResaerch",allTreadApiFirst:"https://www.fastmock.site/mock/0fdbe709330c1a68f26cbef61c777772/graduateSign/api/getAllTread",allPaperApi:"https://www.fastmock.site/mock/0fdbe709330c1a68f26cbef61c777772/graduateSign/api/getAllTread",myPaperApi:"https://www.fastmock.site/mock/0fdbe709330c1a68f26cbef61c777772/graduateSign/api/Mypaper",userInfoApi:"https://www.fastmock.site/mock/0fdbe709330c1a68f26cbef61c777772/graduateSign/api/userInfo",testApi:"https://www.fastmock.site/mock/0fdbe709330c1a68f26cbef61c777772/graduateSign/api/test"},mutations:{setUserName:function(e,t){e.username=t},setPassWord:function(e,t){e.password=t},setLogin:function(e,t){e.islogin=t}},actions:{},modules:{}}),f=n("3fd4"),d=(n("7dd6"),n("690e"),n("ed2c"),Object(r["createApp"])(u));d.use(l).use(s["a"]).use(f["c"]).mount("#app")},e80d:function(e,t,n){"use strict";n("52ba")},ed2c:function(e,t,n){}});
//# sourceMappingURL=app-legacy.665b0b77.js.map