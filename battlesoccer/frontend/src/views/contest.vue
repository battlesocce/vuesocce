<template><div class="ody">
<div class="home"></div><br><br>
     <center><h1>Terms and Conditions</h1></center><br>
    <div class="container text-center">
	<div class="row  text-center" >
		<div class="col-md-12 col-md-offset-2">
			<form name="tandc" ng-submit="approveTandC()">
				<div class="panel panel-default" style="margin-top:20px; margin:auto">
					<div class="panel-body" style="max-height:500px; overflow-y:scroll; background-color:white; " >
						<div style="text-align:center;">
							<p> 
                            <center><h5>Effective on June 6, 2020</h5></center>
<h4><center>Battlesoccer, Terms of Service</center></h4>

Welcome to Battlesoccer! Thank you for using the Battlesoccer.in and for taking the time to read this document. Battlesoccer.in ( "we", "us", and/or “our”)
provides a Turf booking and online tournament , matchmaking services  through the website Battlesoccer.in as well as other websites owned or operated by
Battlesoccer. Your use of the Battlesoccer Service provided through or in connection with the Sites and  Apps . Your viewing and usage of the content
available at the Sites and  Apps of Battlesoccer, is subject to these Terms of Service. By agreeing to these Terms of Service, you consent to
Battlesoccer's collection, use and disclosure of your data, including your personally identifiable information (“PII”),
with respect to your use of the Battlesoccer service. These Terms of Service govern access to and use of the Battlesoccer Service and any content,
information, products or services therein, by all users and content providers. This is a legal agreement between you and Battlesoccer.
IF YOU DO NOT ACCEPT THESE TERMS OF SERVICE IN THEIR ENTIRETY, YOU MAY NOT ACCESS OR USE OR LINK YOUR CONTENT ON THE BATTLESOCCER SERVICE.
IF YOU ARE ACCESSING AND USING THE BATTLESOCCER SERVICE ON BEHALF OF A COMPANY OR OTHER LEGAL ENTITY, YOU REPRESENT THAT YOU HAVE THE AUTHORITY
TO BIND THAT COMPANY OR OTHER LEGAL ENTITY TO THESE TERMS OF SERVICE, AND ALL REFERENCES TO “YOU” IN THESE TERMS OF SERVICE APPLY TO THE COMPANY OR
LEGAL ENTITY.
<br>
IMPORTANT NOTICE REGARDING ARBITRATION: WHEN YOU AGREE TO THESE TERMS OF SERVICE YOU ARE AGREEING (WITH LIMITED EXCEPTION) TO RESOLVE ANY DISPUTE
BETWEEN YOU AND BATTLESOCCER THROUGH BINDING, INDIVIDUAL ARBITRATION RATHER THAN IN COURT. PLEASE REVIEW CAREFULLY SECTION 13
“DISPUTE RESOLUTION FOR CONSUMERS” BELOW FOR DETAILS REGARDING ARBITRATION (INCLUDING THE PROCEDURE TO OPT OUT OF
                            <br>
1. General
<br>
Third-Party Links on the Battlesoccer.in
The websites displayed as advertisements or linked to by the Battlesoccer Service are owned and operated by individuals and/or companies over
whom Battlesoccer exercises no control. Battlesoccer assumes no responsibility for the content of any website or other resource included in any
advertisements or otherwise linked to by the Battlesoccer Service. As an example, logos as well as links to other websites in the form of advertisements
are the copyright or trademarks of each respective website or entity giving the advertisement. If, for any reason, the owner and operator of a
linked website wishes the link from the Battlesoccer Service to be deleted, they must contact Battlesoccer and expressly request such deletion.

Personal Use Only
                            <br>
The Battlesoccer Service is made available for your personal, non-commercial use only. Use of Battlesoccer to book bulk slots and selling them,
or to increase traffic to your website for commercial reasons, such as advertising sales is expressly forbidden. You may not take the results,ideas,or anything
copyrighted from Battlesoccer.in and reformat and display them, or mirror the Battlesoccer home page or any pages from Battlesoccer.in on your website,
or send automated queries,tournament entering ,account creation or slotbooking to Battlesoccer system without express permission from Battlesoccer.
<br>
If you wish to make commercial use of the Battlesoccer Service you must enter into an agreement with Battlesoccer to do so.
Please contact battlesoccer for more information.
<br>
2.Tournament<br>
By Entering a tournament organised by Battlesoccers you agree to the terms of service and also the guidelines and rules given by Battlesoccer to organise
the tournament.If found to be violating the rules battlesoccer can immediatly terminate you and your team from the tournament without any further questions
and refund will not be given.If found to create problems after termination from the tournament battlesoccer has the rights to take legal action against you.
Once you have registered for the tournament by paying , the payment will not be refunded under any circumstances unless Battlesoccer decides to refund it.
Refrees will be arranged by Battlesoccer or anyother entity to whom battlesoccer has given the consent/permission to do so.Battlesoccer can change the
refree whenever it pleases to do so(even in between the match).Battlesoccer may terminate a player or disqualify the whole team if  found to be cheating
when playing or trash talking the other team/teams.
Rules to follow during the tournament:
                            <br>
*Refrees decision will be final in the match.<br>
*Players have to arrive on time for the match as per the slots given for them<br>
*Only 6 players are allowed to play for a team at a time in the field, however they can have 2 substituition changes<br>
Any damage caused to the turf or any property is the sole responsibility of the individual or the team which has caused the damage.<br>
Battlesoccer is not responsible in any way for your belongings when it is damaged or lost.It is your responsibility to take care of your
belongings.The tournament prizes ,venue ,and timings can be changed anytime by battlesoccer without prior notice.
<br><br>
						</div>
					</div>
				</div>
<!--				<div style="text-align:center;" ng-if="settings.Authentication.RequireTermsAndConditions && !UserInfo.approvedTermsAndConditions && UserInfo.isAuthenticated">-->
<!--					<button style="margin:20px;" class="btn btn-primary" type="submit">Agree to Terms and Conditions</button>-->
<!--				</div>-->
			</form>
		</div>
	</div>
</div>
<br>
<br>
<center><button type="submit" class="button1"><h1>Join Battle Takedown Now</h1></button></center>
<br>
<br>
<h1><center>Teams Enrolled</center></h1>
<br>
</div>
</template>

<script>
export default {
    name:"contest"
}
</script>

<style scoped>
.button1 {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
  left:50%;
}

.home {
    width: 100%;
    height: 100vh;
    background-image:url('~@/assets/img/contest-min.png') ;
    background-position: center top;
	  background-size:cover;
}
</style>