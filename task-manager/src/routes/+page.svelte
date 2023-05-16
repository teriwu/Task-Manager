<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<script>
	import { Alert } from 'flowbite-svelte';
</script>

<svelte:head>
	<title>Task Manager</title>
	<meta name="description" content="Task manager app in the making" />
  <style>
    /* @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap'); */
    /* <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet"> */
  </style>
</svelte:head>

<div class="p-8">
	<Alert>
		<span class="font-medium">Info alert!</span> Change a few things up and try submitting again.
	</Alert>
</div>

<section>
  <div class="container mx-auto max-w-lg h-[600px] p-4 border-solid border-black rounded-lg shadow-lg">
    <p class="text-2xl font-bold text-center font-pacifico">Heading Test</p>
  </div>
</section>