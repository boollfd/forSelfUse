<template>
  <div id="wrapper">

    <div id="swiper"  @click="moving" @touchMove="touched">
        <img :src='"@/assets/img/swiper/"+num+".png"' v-for="num in nums"/>
    </div>

    <div class="nav">
        <div v-for="i in nums.length" class="nav-item" :class="{imgActive:i===nums[0]}" :index="i"></div>
    </div>

  </div>
</template>

<script>
export default {
name: "Swiper",
  data(){
  return{
    left:0,
    nums:[1,2,3,4]
  }
  },
  mounted() {
    var swiperInterval = setInterval(this.moving,3000)
  },
  methods:{
    moving () {
      this.nums.push(this.nums.shift())
    },
    touched(){
      clearInterval(swiperInterval)
    }
    }
}
</script>

<style scoped>
#swiper{
  position: relative;
  justify-content: left;
  display: flex;
}
#wrapper{
  width: 100%;
  overflow: hidden;
}

#swiper img{
  width: 100%;
  flex: 0;
}
.nav{
  display: flex;
  justify-content: center;
  position: relative;
  width: 100%;
  bottom: 18px;

}
.nav-item{
  box-sizing: border-box;
  border-radius: 4px;
  width: 8px;
  height: 8px;
  z-index: 1;
  background-color: white;
  margin:0 2px;
}
.imgActive{
  background-color: red;
}
</style>
