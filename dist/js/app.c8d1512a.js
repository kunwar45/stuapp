(()=>{const e=Vue.createApp({data(){return{color:"yellow",size:18,showThemes:!1,isHighlighted:!1}},methods:{toggleThemes(){this.showThemes=!this.showThemes},toOffWhite(){this.color="yellow"},toBlackWhite(){this.color="blue"},changeFontSize(e){console.log(e),this.size=e},highlight(){this.isHighlighted=!this.isHighlighted}}});e.mount("#app")})();
//# sourceMappingURL=app.c8d1512a.js.map