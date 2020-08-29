<template>
  <div>
<body class="profile-page">
    <div ><img :src="team.coverpic" class="responsive" style="margin-top:62px;" >
    </div>
    <div class="main main-raised">
		<div class="profile-content">
            <div class="container">
                <div class="row">
	                <div class="col-md-6 ml-auto mr-auto">
        	           <div class="profile">
	                        <div class="avatar">
	                            <img :src="team.logo" alt="Circle Image" class="img-raised rounded-circle img-fluid">
                          </div>
	                        <div class="name">
	                            <h3 style="font-size:5vw;">{{team.teamname | capitalize}}</h3>
	                        </div>
	                    </div>
    	            </div>
                </div>
                    <h3 style="font-size:3vw;"><center>{{team.teamquotes| capitalize}}</center></h3>
                <br><br>
             <br>
</div>
<div style="overflow-x:auto;">
  <table class="table">
      <tr>
          <th><h4><center>Match</center></h4></th>
          <th><h4><center>Goal</center></h4></th>
          <th><h4><center>Goal</center></h4></th>
          <th><h4><center>Date</center></h4></th>
          <th><h4><center>won</center></h4></th>

      </tr>
    <tbody>
      <tr v-for="teampresent in team.belongs"
      :key="teampresent.id">

          <td><h5><center>{{teampresent.team_b}}</center></h5></td>
          <td><h5><center>{{teampresent.team_a_goals}}</center></h5></td>
          <td><h5><center>{{teampresent.team_b_goals}}</center></h5></td>
          <td><h5><center>{{teampresent.date }}</center></h5></td>
          <td><h5><center>{{teampresent.winner}}</center></h5></td>

      </tr>
   </tbody>
  </table> 
            </div>
		</div>
    </div>
</body>
<br>
        </div> 
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default{
  name: "matchplayed",
  
  data() {
    return {
      team: {},
      id:null,
      error: null
    }
  },
   methods: {
      getmatchdetails() {
      let endpoint = `/api/team/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data;
          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    }
   },
 created() {
    this.id = this.$route.params.id;
    this.getmatchdetails()
    },

}
</script>
<style scoped>
@import '../assets/css/details.css';
body {

    font-family: "Quicksand", sans-serif;

}
.upload-btn-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
}



.upload-btn-wrapper input[type=file] {
  font-size: 100px;
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}
.responsive{
width:100%;
height:auto;

}
</style>
