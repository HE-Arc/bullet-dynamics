<template>
  <v-card class="mx-auto" max-width="500" outlined>
    <v-card-title>Configurations</v-card-title>
    <v-list rounded>
      <v-list-item
        v-for="(config, i) in configs"
        :key="i"
      >
        <v-list-item-content>
          <SimulatorConfigElement :config="config" />
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
  data() {
    return {};
  },
  props: ["configs"],
};
</script>
