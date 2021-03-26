<template>
  <v-card class="mx-auto" max-width="500" outlined>
    <v-card-title> config list </v-card-title>
    <v-list rounded>      
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
        >
          <v-list-item-content>
            <SimulatorConfigElement :name="item.name"/>
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
    items: [
      {
        name: "config 1",
      },
      {
        name: "config 2",
      },
      {
        name: "config 3",
      },
    ],
  }),
};
</script>
