<template>
  <v-app style="
    background: #3A1C71;
    background: -webkit-linear-gradient(to right,#F2D7D5, #F5B7B1, #EBDEF0 , #E8DAEF);
    background: linear-gradient(to right, #F2D7D5, #F5B7B1, #EBDEF0 , #E8DAEF);
  ">
    <v-app-bar
      app
      style="#C39BD3"
      light
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"  
          class="shrink mr-2"
          contain
          src="https://static.tradinghours.com/logos/bse-bombay.png"
          transition="scale-transition"
          width="150"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="110"
          transition="scale-transition"
          src="https://miro.medium.com/max/1130/1*aKt1yw66P-70alNCFHFEbQ.jpeg"
          width="100"
        />
        
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href=" https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Data</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <DatatableComponent/>
    </v-main>
  </v-app>
</template>

<script>
// import DatatableSecondComponent from './components/DatatableSecondComponent';
import DatatableComponent from './components/DatatableComponent';
export default {
  name: 'App',
  
  components: {
    DatatableComponent,
  },
  data: () => ({
    //
  }),
};
</script>

