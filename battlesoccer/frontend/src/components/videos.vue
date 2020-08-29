<template>
<div clas="ody">
 <br><br><br>
            <div class="right2">
    <h3 >Create your team today</h3>
    <h4>Stop looking at the Highlights</h4>
    Come on let us battle on the real field and Create One!!<br>
    <h4 class="quotes">"Play to learn, learn to burn"</h4>
  </div>
<br><br>
 <div class="container">
    <h1>Hightlights</h1>   
 </div>
    <br>
        <div v-for = "video in highligths"
        :key="video.pk">
            <div class="videocover">
  <video :src="video.highlight" controls autoplay loop  muted>
</video>
<br>        
 <center><h4>{{video.teamname| capitalize}}</h4></center>
        </div>
          </div>
<br><br>
</div>
</template>

<script>

import { apiService } from "@/common/api.service.js";
export default{
  name: "videos",
  data() {
    return {
      highligths: [],
    }
  },
   methods: {
      gethighligthsData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/highlights/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.highligths = data;
            this.highligths = this.highligths.slice(0,4);
          } else {
            this.highligths = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    },
  created() {
    this.gethighligthsData()
    }
}
</script>
<style scoped>

.videocover {
  color:black;
  overflow:hidden;
  float:left;
  width:25%;
  padding: 0 4px;

}

video{
width:100%;
margin:auto;
font-size:35px;

}


@media only screen and (max-width:950px) {
   .videocover {
    width:50%;
  }
}


.right2 {
  color:black;
  float:left;
  width:100%;
  padding:18px;
  margin-top:-120px;
  margin-bottom:20px;
  text-align:center;
}
</style>
