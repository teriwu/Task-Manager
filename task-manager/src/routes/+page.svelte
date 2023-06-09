<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<script>
	import { Alert } from "flowbite-svelte";
  import { Footer, FooterCopyright, FooterLinkGroup, FooterLink } from "flowbite-svelte";
</script>

<svelte:head>
	<title>Task Manager</title>
	<meta name="description" content="Task manager app in the making" />
  <style>
    /* @import url("https://fonts.googleapis.com/css2?family=Pacifico&display=swap"); */
    /* <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet"> */
  </style>
</svelte:head>

<div class="p-8">
	<Alert>
		<span class="font-medium">Info alert!</span> Change a few things up and try submitting again.
	</Alert>
</div>

<!-- <Skeleton class="py-4" />
<ImagePlaceholder class="py-4" />

<Banner id="default-banner" position="absolute">
  <p class="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">
    <span class="inline-flex p-1 mr-3 bg-gray-200 rounded-full dark:bg-gray-600">
      <svg
        class="w-4 h-4 text-gray-500 dark:text-gray-400"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
        aria-hidden="true">
        <path
          d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
      </svg>
      <span class="sr-only">Light bulb</span>
    </span>
    <span
      >Default sticky banner that supports hyperlinks like this ➡️<a
        href="https://flowbite.com"
        class="inline font-medium text-blue-600 underline dark:text-blue-500 underline-offset-2 decoration-600 dark:decoration-500 decoration-solid hover:no-underline"
        >Flowbite Library</a
      ></span>
  </p>
</Banner> -->

<section>
  <div class="container mx-auto max-w-lg h-[600px] p-4 border-solid border-black rounded-lg shadow-lg">
    <p class="text-2xl font-bold text-center font-pacifico">Heading Test</p>
  </div>
</section>


<!-- Temporary footer -->
<Footer>
  <FooterCopyright href="/" by="Flowbite™" year={2023} />
  <FooterLinkGroup ulClass="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
    <FooterLink href="/">About</FooterLink>
    <FooterLink href="/">Privacy Policy</FooterLink>
    <FooterLink href="/">Licensing</FooterLink>
    <FooterLink href="/">Contact</FooterLink>
  </FooterLinkGroup>
</Footer>