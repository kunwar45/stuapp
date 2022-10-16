const app = Vue.createApp({
    // data, functions etc
    // template: '<h2>I am the template</h2>',
    data() {
      return {
        color: 'yellow',
        size: 18
      }
    },
    methods: {
        toOffWhite(){
            this.color = 'yellow'
        },
        toBlackWhite(){
            this.color = 'white'
        },
        changeFontSize(size){
            console.log(size)
            this.size = size
        }
    }
  })
  
  app.mount('#app')