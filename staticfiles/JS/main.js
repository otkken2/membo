// var myVue = new Vue({
//     el:'#app',
//     data:{
//         gnavShow: true,
//         humIconShow: false,
//         winWidth: window.innerWidth,
//     },
//     created:function(){
//         addEventListener('resize', this.gnavSwitch);
//     },
//     beforeDestroy:function(){
//         removeEventListener('resize', this.gnavSwitch);
//     },
//     methods:{
//         humIconClick:function(){
//             this.gnavShow = !this.gnavShow;
//             console.log('vue')
//         },
//         gnavSwitch:function(){
//             if (this.winWidth > 740 && (this.gnavShow = false)){
//             // if (this.winWidth > 740){
//                 this.gnavShow = !this.gnavShow;
//                 console.log('hello from gnavSwitch');
//             }
//         },
//     },
// })



// $(function(){
//     if (window.innerWidth < 740){
//         $('.header-menus').hide();
//         console.log('innerwidth is less than 740!');
//     } else {
//         console.log('innerwidth is wider than 740!');
//     }
//     $('.hamburger').click(function(){
//         $('.header-menus').toggle(180);
//         // console.log("live jq");
//     })
//     console.log("hello!from jq")
// });

$(function(){$('.hamburger').click(function(){
    $('.header-menus').slideToggle(200);
    // var $css = $('.header-menus').css('display');
    console.log('hello');
    });
});