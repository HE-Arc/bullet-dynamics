<template>
  <div>
    <v-container class="grey lighten-5" fluid>
      <v-row v-if="!loadingData" justify="space-between">
        <v-col cols="4">
          <v-container>
            <v-row justify="space-between">
              <v-col>
                <SimulatorConfigList :configs="configs" />
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
      <v-row v-else>
        <v-spacer></v-spacer>
        <v-col>
          <v-card style="margin: 20px; padding: 10px">
            <v-card-subtitle style="text-align: center">
              <h2>CONFIGURATION</h2>
              <div style="margin: 15px 0">Loading data</div>
            </v-card-subtitle>
            <v-card-text style="text-align: center">
              <v-progress-circular
                :size="70"
                :width="7"
                color="primary"
                indeterminate
              ></v-progress-circular>
            </v-card-text>
          </v-card>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import GraphComponent from "../components/GraphComponent.vue";
import SimulatorConfigList from "../components/SimulatorConfigList.vue";
import SimulatorParamList from "../components/SimulatorParamList.vue";
import { getAPI } from "../plugins/axios-api";
//import { mapState } from "vuex";

export default {
  name: "Simulator",
  components: {
    SimulatorConfigList,
    SimulatorParamList,
    GraphComponent,
  },
  data() {
    return {};
  },
  computed: {
    loadingData() {
      return this.configs.length <= 0;
    },
    configs() {
      return Object.values(this.$store.state.configs);
    },
  },
  methods: {
    loadConfigs() {
      let _this = this;

      this.configs = [];
      this.loadingConfigs = true;

      let username = this.$store.state.username;
      //console.log(username);

      getAPI
        .get(`/api/users/${username}/`, {
          headers: {
            Authorization: `Bearer ${_this.$store.state.accessToken}`,
          },
        })
        .then((response) => {
          console.log("Getting configs");
          _this.configs = response.data.config;
          console.log(_this.configs);
        })
        .catch((err) => {
          console.log(err);
        })
        .then(() => {
          _this.loadingConfigs = false;
        });
    },
  },
  created: function () {
    this.loadConfigs();
  },
};
</script>
