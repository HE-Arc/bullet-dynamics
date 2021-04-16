<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="2">{{ name }}: </v-col>
      <v-col cols="12" sm="8">
        <v-progress-linear
          v-model="progress"
          :color="color"
          height="25"
        ></v-progress-linear>
      </v-col>
      <v-col cols="12" sm="2">{{ total }} {{ unit }}</v-col>
    </v-row>
  </v-container>
</template>


<script>
export default {
  name: "GunProgressBar",
  data() {
    return {};
  },
  props: ["name", "unit", "color", "total", "progress"],
};
</script>