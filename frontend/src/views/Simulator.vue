<template>
  <div>
    <v-container class="grey lighten-5" fluid>
      <v-row justify="space-between">
        <v-col cols="12" md="4">
          <v-container>
            <v-row justify="space-between">
              <v-col style="max-height: 800px" class="overflow-y-auto">
                <SimulatorConfigList :configs="configs" />
                <!--TODO message : no configs  -->
              </v-col>
            </v-row>
            <v-row justify="space-between">
              <v-col>
                <SimulatorParamList />
              </v-col>
            </v-row>
          </v-container>
        </v-col>
        <v-col cols="12" md="8">
          <v-container>
            <v-row justify="space-between">
              <v-col>
                <GraphComponent
                  name="Graph of bullet drop by horizontal distance"
                />
              </v-col>
            </v-row>
          </v-container>
        </v-col>
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
import SimulatorConfigList from "@/components/SimulatorConfigList.vue";
import SimulatorParamList from "@/components/SimulatorParamList.vue";
import SnackbarInfo from "@/components/SnackbarInfo.vue";

export default {
  name: "Simulator",
  components: {
    SimulatorConfigList,
    SimulatorParamList,
    GraphComponent,
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

    if (configs.length <= 0) this.$store.dispatch("fetchConfigs");
  },
};
</script>
