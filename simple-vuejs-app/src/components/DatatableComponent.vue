<template>
  <div class="">

    <v-main>
    <form>
    
    <v-container>
    
    <v-row>
      <v-col
        cols="12"
        lg="6"
      >
      
          
            <v-text-field
      v-model="name"
      :error-messages="nameErrors"
      :counter="100"
      label="Name"
      required = false
      @input="readDataFromAPI"
      @blur="$v.name.$touch()"
    ></v-text-field>
         
          
       
      </v-col>

      <v-col
        cols="12"
        lg="6"
      >
        <v-menu
        v-model="menu2"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="date"
            label="Date Of Equity"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
            @input="$v.date.$touch()"
            
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="date"
          @input="menu2 = false"
          @change = "readDataFromAPI"
        ></v-date-picker>
      </v-menu>
      </v-col>
      <v-col
        cols="12"
        lg="6"
      ><v-btn class="mr-4" @click="readDataFromAPI">Submit</v-btn> <v-btn class="mr-4" @click="clear">Clear</v-btn></v-col>
      
    </v-row>
  </v-container>
  </form>
    </v-main>
    <v-data-table 
    
      :page="page"
      :pageCount="total_pages"
      :headers="headers"
      :items="equity_data"
      :options.sync="options"
      :server-items-length="total_data"
      :loading="loading"
    >
    <template v-slot:item.OPEN="{ item }">
      <v-chip
        :color="getColor(item.OPEN)"
        dark
      >
        {{ item.OPEN }}
      </v-chip>
      </template>

      <template v-slot:item.CLOSE="{ item }">
      <v-chip
        :color="getColor(item.CLOSE)"
        dark
      >
        {{ item.CLOSE }}
      </v-chip>
      </template>

      <template v-slot:item.HIGH="{ item }">
      <v-chip
        :color="getColor(item.HIGH)"
        dark
      >
        {{ item.HIGH }}
      </v-chip>
      </template>

  <template v-slot:item.LOW="{ item }">
      <v-chip
        :color="getColor(item.LOW)"
        dark
      >
        {{ item.LOW }}
      </v-chip>
</template>
      <template v-slot:item.SC_NAME="{ item }">
      <v-chip
        
        dark
      >
        {{ item.SC_NAME }}
      </v-chip>
      </template>

      <template v-slot:item.SC_CODE="{ item }">
      <v-chip
        
        dark
      >
        {{ item.SC_CODE }}
      </v-chip>
      </template>

      
    </v-data-table>
    
  </div>
</template>
<style scoped></style>
<script>
import axios from "axios";
// import form_value from "./form_for_filter"; 
  import { validationMixin } from 'vuelidate'
  import { required, maxLength } from 'vuelidate/lib/validators'
  
export default {
  name: "DatatableComponent",
  mixins: [validationMixin],

    validations: {
      name: { required, maxLength: maxLength(100) }
      
    },

  data() {
    return {
      
        //for form 
    valid: true,
      name: '',
      nameRules: [
        // v => !!v || 'Name is required',
        v => (v && v.length <= 100) || 'Name must be less than 100 characters',
      ],
      
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
      checkbox: false,
    //form ends


      page: 1,
      total_data: 0,
      total_pages: 0,
      equity_data: [],
      loading: true,
      options: {},
      headers: [
        { text: "CODE", value: "SC_CODE" },
        { text: "NAME", value: "SC_NAME" },
        { text: "OPEN", value: "OPEN" },
        { text: "HIGH", value: "HIGH" },
        { text: "LOW", value: "LOW" },
        { text: "CLOSE", value: "CLOSE" },
      ],
    };
  },


  computed: {
     
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 100 characters long')
        // !this.$v.name.required && errors.push('Name is required.')
        return errors
      },
     
    },
  watch: {
    options: {
      handler() {
        this.readDataFromAPI();
      },
    },
    deep: true,
  },
  methods: {
    async readDataFromAPI() {
        var name=this.name
        var date=this.date
      this.loading = true;
      const { page, itemsPerPage } = this.options;
      console.log("Page Number ", page, itemsPerPage);
      let pageNumber = page - 1;
      var queryParam = ''
        if(itemsPerPage){
          if(queryParam == '')
          {
              queryParam=queryParam+'?'+"size="+ itemsPerPage
              }
          else{
              queryParam=queryParam+'&'+"size="+ itemsPerPage
          }
      }
      if(pageNumber!= undefined){
          if(queryParam == '')
          {
              queryParam=queryParam+'?'+"page="+ pageNumber
              }
          else{
              queryParam=queryParam+'&'+"page="+ pageNumber
          }
      }
      if(name!= undefined && name!= ''){
          if(queryParam == '')
          {
              queryParam=queryParam+'?'+"name="+ name
              }
          else{
              queryParam=queryParam+'&'+"name="+ name
          }
      }
      if(date!= undefined && date!=''){
          if(queryParam == '')
          {
              queryParam=queryParam+'?'+"date="+ date
              }
          else{
              queryParam=queryParam+'&'+"date="+ date
          }
      }
      
      // var baseurl = "https://api.instantwebtools.net/v1/passenger"
      var baseurl = `${window.location.origin}/cache/data/`
      var url = baseurl + queryParam
      // const headers = { "Content-Type": "application/json" };
      await axios.get(url).then((response) => {
          this.loading = false;
          this.equity_data = response.data.data;
          this.total_data = response.data.total_data;
          this.total_pages = response.data.total_pages;
        });
    },
    
      clear () {
        this.$v.$reset()
        this.name = ""
        this.date = new Date().toISOString().substr(0, 10)
        
      },
      
      getColor (calories) {
        if (calories > 1000) return 'red'
        else if (calories > 500) return 'orange'
        else return 'green'
      },
      
  },
  mounted() {
    this.readDataFromAPI();
  },
};
</script>