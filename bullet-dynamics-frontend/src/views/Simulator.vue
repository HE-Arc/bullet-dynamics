<template>
  <div>
    <v-container>
      <v-row justify="space-between">
        <v-col cols="4">
          <v-container>
            <v-row justify="space-between">
              <v-col>
                <SimulatorConfigList :configs="this.configs" />
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
import { getAPI } from "../plugins/axios-api";
//import { mapState } from "vuex";

export default {
  name: "Simulator",
  data() {
    return {
      configs: [],
    };
  },
  components: {
    SimulatorConfigList,
    SimulatorParamList,
    GraphComponent,
  },
  //computed: mapState(["APIData"]),
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
