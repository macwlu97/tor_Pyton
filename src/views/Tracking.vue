<template>
<div>
    <v-container grid-list-md>
       
      <v-card class="white">
    
          <!-- <div class="map"> 
            <div class="tracking"> 
              </div>
            </div> -->
        <div id="outerspace">
<div class="kurier">
<div><!-- rocket --></div>
Tracking paczki
</div>#Mapa
</div>
      </v-card>
    </v-container>
  </div> 
</template>

<script>
export default {
  name: "Tracking",
};
</script>

<style scoped>
.white {
  height: 50vw;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif
}
#outerspace {
    position: relative;
    height: 400px;
    background: #0c0440 url('../assets/map.jpg');
    color: #000;
  }
  div.kurier {
    position: absolute;
    bottom: 10px;
    left: 20px;
    -webkit-transition: 3s ease-in;
    -moz-transition: 3s ease-in;
    -o-transition: 3s ease-in;
    transition: 3s ease-in;
  }
  div.kurier div {
    width: 2vw;
    height: 2vw;
    background-color: brown;
    border-radius: 1vw;
    color: #000;
    -webkit-transition: 2s ease-in-out;
    -moz-transition: 2s ease-in-out;
    -o-transition: 2s ease-in-out;
    transition: 2s ease-in-out;
  }

  /* hover final state */
  #outerspace:hover div.kurier {
    -webkit-transform: translate(540px,-200px);
    -moz-transform: translate(540px,-200px);
    -o-transform: translate(540px,-200px);
    -ms-transform: translate(540px,-200px);
    transform: translate(540px,-200px);
  }
  #outerspace:hover div.rocket div {
    -webkit-transform: rotate(70deg);
    -moz-transform: rotate(70deg);
    -o-transform: rotate(70deg);
    -ms-transform: rotate(70deg);
    transform: rotate(70deg);
  }
</style>