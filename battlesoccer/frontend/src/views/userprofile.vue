<template>
  <div class="ody" v-if="team.coverpic">
    
<div class="profile-page">
    <div ><img :src="team.coverpic" class="responsive" style="margin-top:62px;" >
    </div>
    <div class="main main-raised">
		<div class="profile-content">
            <div class="container">
                <div class="row">
	                <div class="col-md-6 ml-auto mr-auto">
        	           <div class="profile">
	                        <div class="avatar">
                                         <div class="upload-btn-wrapper">
  <button class="btn btn-just-icon btn-link btn-twitter"><li class="fa fa-user-o"></li></button>
  <input type="file" name="myfile" @change="onchange"/>
</div>
	                            <img :src="team.logo" alt="Circle Image" class="img-raised rounded-circle img-fluid">
	                                                  <div class="upload-btn-wrapper">
  <button class="btn btn-just-icon btn-link btn-twitter"><li class="fa fa-picture-o"></li></button>
  <input type="file" name="myfileprofile" @change="onchangeprofile"/>
</div>
                          </div>
	                        <div class="name">
	                            <h3 style="font-size:5vw;">{{team.teamname | capitalize}}</h3>
								                <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'Teamedit' ,params: {id:id}}"
        ><i class="fa fa-edit"></i></router-link>
                                 <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'Addplayer' }"
        ><i class="fa fa-plus"></i></router-link>
        <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'matchplayed',params: {id:id} }"
        ><i class="fa fa-info"></i></router-link>
        <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'gallery',params: {id:id} }"
        ><i class="fa fa-file-video-o"></i></router-link>
	                        </div>
	                    </div>
    	            </div>
                </div>
                    <h3 style="font-size:3vw;"><center>{{team.teamquotes| capitalize}}</center></h3>
                <br><br>
            </div>
		</div>
    </div>
</div>
<br>
<div class="container-sm">
  <br>
      <transition-group name=slide class="row">
         <Player 
        v-for="player in team.players"
        :player="player"
        :user="team.user"
        :requestUser="requestUser"
        :key="player.id"
        @delete-player="deleteplayer"
        @update-pic="updatepic"
      /></transition-group>
</div>
        </div> 
</template>

<script>

import { CSRF_TOKEN } from "@/common/csrf_token.js"
import axios from 'axios'
import { apiService } from "@/common/api.service.js";
import Player from "@/components/player.vue";
export default{
  name: "Userprofile",
     components: {
    Player
  },
  data() {
    return {
      team: {},
      requestUser:null,
      id:null,
      logo: null,
      coverpic: null,
      error: null
    }
  },
   methods: {
     setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
      getTeamData() {
      this.id = window.localStorage.getItem("id");
      this.id=this.id-1
      // get the details of a question instance from the REST API and call setPageTitle
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
    },
 onchange(event){
  this.logo=event.target.files[0]
      // Tell the REST API to create or update a Question Instance
      if (!this.logo) {
        this.error = "You can't send an empty question!";
      }  else {
      const formData = new FormData()
     formData.append('logo', this.logo)
     axios.put( '/api/avatar/',
  formData,
  {
    headers: {
         "Access-Control-Allow-Origin" : "*",
        'Content-Type': 'multipart/form-data',
        "X-CSRFTOKEN": CSRF_TOKEN

    }
  }
).then(function(){
  console.log('SUCCESS!!');
})
.catch(function(){
  console.log('FAILURE!!');
});
setTimeout(() => {
 this.getTeamData()
        },1000)
}
    },
    onchangeprofile(event){
  this.coverpic=event.target.files[0]
      // Tell the REST API to create or update a Question Instance
      if (!this.coverpic) {
        this.error = "You can't send an empty question!";
      }  else {
      const formData = new FormData()
     formData.append('coverpic', this.coverpic)
     axios.put( '/api/avatar/',
  formData,
  {
    headers: {
         "Access-Control-Allow-Origin" : "*",
        'Content-Type': 'multipart/form-data',
        "X-CSRFTOKEN": CSRF_TOKEN

    }
  }
).then(function(){
  console.log('SUCCESS!!');
})
.catch(function(){
  console.log('FAILURE!!');
});
setTimeout(() => {
 this.getTeamData()
        },1500)
}
    },

    async deleteplayer(player) {
      // delete a given answer from the answers array and make a delete request to the REST API
      let endpoint = `/api/player/${player.id}/`;

      try {
        await apiService(endpoint, "DELETE")
        this.$delete(this.team.players,this.team.players.indexOf(player))
      }
      catch (err) {
        console.log(err)
      }
    },
async updatepic(player,pic) {
if (!pic) {
        this.error = "You can't send an empty question!";
      }  else {
      const formData = new FormData()
     formData.append('pic', pic)
     axios.put( `/api/playerpic/${ player.id }/`,
  formData,
  {
    headers: {
         "Access-Control-Allow-Origin" : "*",
        'Content-Type': 'multipart/form-data',
        "X-CSRFTOKEN": CSRF_TOKEN

    }
  }
)
.then(function(){
  console.log('SUCCESS!!');
})
.catch(function(){
  console.log('FAILURE!!');
});
setTimeout(() => {
 this.getTeamData()
        },1000)
      }
    }
},
 created() {
    this.getTeamData()
    this.setRequestUser()
    },

}
</script>
<style scoped>
@import '../assets/css/details.css';

@media screen and (max-width:600px) {

.profile-page .profile img {
    max-width: 120px;
    width: 100%;
    margin: 0 auto;
    -webkit-transform: translate3d(0,-40%,0);
    -moz-transform: translate3d(0,-40%,0);
    -o-transform: translate3d(0,-40%,0);
    -ms-transform: translate3d(0,-40%,0);
    transform: translate3d(0,-40%,0);
}

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
 .slide-leave-active {
        transition: opacity 1s ease;
        opacity: 0;
        animation: slide-out 1s ease-out forwards;
        position: absolute;
    }

    .slide-leave {
        opacity: 1;
        transform: translateX(0);
    }

    .slide-enter-active {
        animation: slide-in 1s ease-out forwards;
    }

    .slide-move
    {
      transition: transform 1s;
    }

    @keyframes slide-out {
        0% {
            transform: translateY(0);
        }
        100% {
            transform: translateY(-30px);
        }
    }

    @keyframes slide-in {
        0% {
            transform: translateY(-30px);
        }
        100% {
            transform: translateY(0);
        }
    }

</style>
