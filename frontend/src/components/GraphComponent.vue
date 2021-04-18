<template>
  <div>
    <v-card v-if="displayedConfigs.length <= 0">
      <v-alert type="info" border="right" colored-border elevation="2">
        <b>Chart:</b> please select a configuration.
      </v-alert>
    </v-card>
    <v-card v-else-if="!loadingData">
      <v-card-title>
        {{ name }}
      </v-card-title>
      <GChart type="LineChart" :data="chartData" :options="chartOptions" />
    </v-card>
    <v-card v-else>
      <loading-screen title="SIMULATION" />
    </v-card>
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";
import LoadingScreen from "./LoadingScreen.vue";

export default {
  name: "GraphComponent",
  components: {
    GChart,
    LoadingScreen,
  },
  data() {
    return {
      chartOptions: {
        chart: {
          title: "title",
          subtitle: "subtitle",
        },
        hAxis: {
          title: "Horizontal distance[m]",
        },
        vAxis: {
          title: "Vertical drop[m]",
        },
        height: 600,
      },
    };
  },
  computed: {
    chartData() {
      if (this.displayedConfigs.length <= 0 || this.simulatorData == null) {
        console.log("YO");
        console.log(this.displayedConfigs);
        return [];
      }
      console.log(this.displayedConfigs);

      const simDataSize = this.simulatorData[0]["data"][0].length;
      const graphData = [];

      let maxX = 0;
      this.simulatorData.forEach((element) => {
        if (this.displayedConfigs.indexOf(element["id"]) >= 0) {
          let tmp = element["data"][0][simDataSize - 1];
          if (maxX < tmp) maxX = tmp;
        }
      });

      //console.log("maxX");
      //console.log(maxX);

      for (let x = 0; x < maxX; ++x) {
        let dataRow = [x];

        this.simulatorData.forEach((element) => {
          if (this.displayedConfigs.indexOf(element["id"]) >= 0) {
            let prevX = 0;
            let nextX = element["data"][0][simDataSize - 1];
            let prevXindex = 0;
            let nextXindex = 0;

            element["data"][0].forEach((val, index) => {
              if (val > prevX && val < x) {
                prevX = val;
                prevXindex = index;
              }
              if (val >= x && val <= nextX) {
                nextX = val;
                nextXindex = index;
              }
            });
            let closestX =
              Math.abs(x - prevX) < Math.abs(x - nextX) ? prevX : nextX;

            let closestIndex = closestX < x ? prevXindex : nextXindex;

            let closestY = element["data"][1][closestIndex];

            dataRow.push(closestY);
          }
        });

        //console.log("dataRow");
        //console.log(dataRow);

        graphData.push(dataRow);
      }

      const titleRow = ["Meters"];
      this.simulatorData.forEach((element) => {
        if (this.displayedConfigs.indexOf(element["id"]) >= 0)
          titleRow.push(element["name"]);
      });
      graphData.unshift(titleRow);

      //console.log("graphData");
      //console.log(graphData);

      return graphData;
    },
    simulatorData() {
      //console.log(this.$store.state.simulatorData);
      return this.$store.state.simulatorData;
    },
    displayedConfigs() {
      return this.$store.state.displayedConfigs;
    },
    loadingData() {
      return this.simulatorData.length <= 0;
    },
  },
  watch: {
    displayedConfigs: function () {},
  },
  created: function () {
    const simulatorData = this.$store.state.simulatorData;

    if (simulatorData.length <= 0) this.$store.dispatch("fetchSimulatorData");
  },
  props: ["name"],
};
</script>
