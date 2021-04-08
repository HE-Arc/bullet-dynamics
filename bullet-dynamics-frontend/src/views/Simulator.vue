<template>
  <div>
    <v-container>
      <v-row justify="space-between">
        <v-col cols="4">
          <v-container>
            <v-row justify="space-between">
              <v-col>
                <SimulatorConfigList />
              </v-col>
            </v-row>
            <v-row justify="space-between">
              <v-col>
                <SimulatorParamList />
              </v-col>
            </v-row>
          </v-container>
        </v-col>
        <v-col cols="8">
          <v-container>
            <v-row justify="space-between">
              <v-col>
                <GraphComponent />
              </v-col>
            </v-row>
            <!--<v-row justify="space-between">
              <v-col>
                <GraphComponent />
              </v-col>
              <v-col>
                <GraphComponent />
              </v-col>
            </v-row>-->
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import GraphComponent from "../components/GraphComponent.vue";
import SimulatorConfigList from "../components/SimulatorConfigList.vue";
import SimulatorParamList from "../components/SimulatorParamList.vue";
import { getAPI } from '../plugins/axios-api';

export default {
  name: "Simulator",
  data () {
    return {
        configs: []
      }
  },
  components: {
    SimulatorConfigList,
    SimulatorParamList,
    GraphComponent,
  },
  methods: {
    loadConfigs() {
      let _this = this;

      // Get loot history
      this.configs = [];
      this.loadingConfigs = true;
      
      getAPI
        .get("/configs/")
        .then(response => {
          console.log('Getting configs');
          _this.configs = response.data;
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        })
        .then(() => {
          _this.loadingConfigs = false;
        });
    },
  },
  created: function () {
    let _this = this;

    _this.loadConfigs();
  }

};
</script>
