<template>
  <v-container>
    <v-row>
      <v-col>
        <h2>{{ name }}</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3" :key="component.id" v-for="component in components">
        <gun-component-card-draggable :type="type" :component="component" />
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
// @ is an alias to /src
import GunComponentCardDraggable from "@/components/GunComponentCardDraggable.vue";

export default {
  name: "GunComponentList",
  components: {
    GunComponentCardDraggable,
  },
  data() {
    return {};
  },
  computed: {
    imgSrc() {
      if (this.name == "Platforms") return "gun";
      else if (this.name == "Ammunition") return "ammunition";
      else return "cannon";
    },
    type() {
      if (this.name == "Platforms") return "platform";
      else if (this.name == "Ammunition") return "ammunition";
      else return "cannon";
    },
  },
  methods: {
    tooltip(component) {
      if (this.name == "Platforms") {
        return (
          component.desc +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$, " +
          component.length +
          "cm"
        );
      } else if (this.name == "Ammunition") {
        return (
          component.desc +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$"
        );
      } else {
        return (
          component.desc +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$, " +
          component.length +
          "cm"
        );
      }
    },
  },
  props: ["name", "components"],
};
</script>