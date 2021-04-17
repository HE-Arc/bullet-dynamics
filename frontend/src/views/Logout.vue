<template>
  <div>
    Logged out
  </div>
</template>

<script>
  export default {
    name: 'Logout',
    created () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'Login' })
        })
    }
  }
</script>

<style>
</style>