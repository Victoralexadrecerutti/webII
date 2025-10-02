<script setup>
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Início</RouterLink>
      <RouterLink to="/page2">Página 2</RouterLink>
      <RouterLink to="/about">Sobre</RouterLink>
    </nav>
  </header>

  <main>
    <RouterView />
  </main>

</template>