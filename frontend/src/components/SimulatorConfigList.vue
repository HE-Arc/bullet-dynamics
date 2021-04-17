<template>
  <v-card class="mx-auto" max-width="500" outlined>
    <v-card-title> config list </v-card-title>
    <v-list rounded>      
        <v-list-item
          v-for="(config, i) in configs"
          :key="i"
        >
          <v-list-item-content>
            <SimulatorConfigElement :name="config.name"/>
          </v-list-item-content>
        </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
import SimulatorConfigElement from "@/components/SimulatorConfigElement.vue";

export default {
  name: "SimulatorConfigList",
  
  components: {
    SimulatorConfigElement,
  },

  data: () => ({ 
  }),

  props: ['configs'],

  created: function () {
    let _this = this;

    console.log(_this.configs);
  },
};
</script>
