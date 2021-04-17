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
          <loading-screen />
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-container>

    <snackbar-info
      :snackbar="snackbar"
      :timeout="snackbarTimeout"
      :text="snackbarText"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import GraphComponent from "@/components/GraphComponent.vue";
import LoadingScreen from '@/components/LoadingScreen.vue';
import SimulatorConfigList from "@/components/SimulatorConfigList.vue";
import SimulatorParamList from "@/components/SimulatorParamList.vue";
import SnackbarInfo from "@/components/SnackbarInfo.vue";

export default {
  name: "Simulator",
  components: {
    SimulatorConfigList,
    SimulatorParamList,
    GraphComponent,
    LoadingScreen,
    SnackbarInfo,
  },
  data() {
    return {
      snackbar: false,
      snackbarText: "Something happened.",
      snackbarTimeout: 2000,
    };
  },
  computed: {
    loadingData() {
      return (
        this.$store.state.platforms.length <= 0 ||
        this.$store.state.ammos.length <= 0 ||
        this.$store.state.cannons.length <= 0
      );
    },
    configs() {
      return Object.values(this.$store.state.configs);
    },
  },
  watch: {
    configs: function () {
      this.snackbarText = "Configurations updated.";
      this.snackbar = true;
    },
  },
  created: function () {
    const configs = this.$store.state.configs;
    const platforms = this.$store.state.platforms;
    const ammos = this.$store.state.ammos;
    const cannons = this.$store.state.cannons;

    if (configs.length <= 0) this.$store.dispatch("fetchConfigs");
    if (platforms.length <= 0) this.$store.dispatch("fetchPlatforms");
    if (ammos.length <= 0) this.$store.dispatch("fetchAmmos");
    if (cannons.length <= 0) this.$store.dispatch("fetchCannons");
  },
};
</script>
