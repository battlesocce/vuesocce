<template>
<div class="ody">
 <br><br><br>
 <div class="container">
    <h1 class="display-4">Hightlights</h1>   
 </div>
    <br>
        <div v-for = "video in highligths"
        :key="video.pk">
            <div class="videocover">
  <video :src="video.highlight" controls autoplay loop  muted>
</video>
 <center><h4>{{video.teamname| capitalize}}</h4></center>

        </div>
          </div>

</div>
</template>

<script>

import { apiService } from "@/common/api.service.js";
export default{
  name: "Highlight",
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


</style>
