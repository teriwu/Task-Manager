<script>
	import { Alert } from "flowbite-svelte";
  import { Footer, FooterCopyright, FooterLinkGroup, FooterLink } from "flowbite-svelte";
  import { Tabs, TabItem } from "flowbite-svelte";

  let newItem = '';
	
  let todoList = [{text: 'Write my first post', status: true},
                  {text: 'Upload the post to the blog', status: false},
                  {text: 'Publish the post at Facebook', status: false}];

function addToList() {
  todoList = [...todoList, {text: newItem, status: false}];
  newItem = '';
}

function removeFromList(index) {
  todoList.splice(index, 1)
  todoList = todoList;
  }

</script>

<svelte:head>
	<title>Task Manager</title>
	<meta name="description" content="Task manager app in the making" />
  <style>
    /* @import url("https://fonts.googleapis.com/css2?family=Pacifico&display=swap"); */
    /* <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet"> */
    h1 {
      font-family: "Pacifico", sans-serif;
    }
  </style>
</svelte:head>

<div class="p-8">
	<Alert>
		<span class="font-medium">Info alert!</span> Change a few things up and try submitting again.
	</Alert>
</div>

<section>

  <Tabs class="container mx-auto max-w-lg">
    <TabItem open title="High">
      <div class="container mx-auto max-w-lg h-[600px] p-4 border-solid border-black rounded-lg shadow-lg">
        <h1 class="text-2xl font-bold text-center font-pacifico">Todo</h1>
        <div class="mx-auto">
          <input bind:value={newItem} type="text" placeholder="new todo item..">
          <button on:click={addToList}>Add</button>
          
          <br/>
          {#each todoList as item, index}
            <input bind:checked={item.status} type="checkbox">
            <span class:checked={item.status}>{item.text}</span>
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <span on:click={() => removeFromList(index)}>❌</span>
            <br/>
          {/each} 
          
          <style> 
            .checked {
                  text-decoration: line-through;
              }
          </style>
        </div>
      </div>
    </TabItem>
    <TabItem open title="Medium">
      <div class="container mx-auto max-w-lg h-[600px] p-4 border-solid border-black rounded-lg shadow-lg">
        <p class="text-2xl font-bold text-center font-pacifico">Todo</p>
        <div class="mx-auto">
          <input bind:value={newItem} type="text" placeholder="new todo item..">
          <button on:click={addToList}>Add</button>
          
          <br/>
          {#each todoList as item, index}
            <input bind:checked={item.status} type="checkbox">
            <span class:checked={item.status}>{item.text}</span>
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <span on:click={() => removeFromList(index)}>❌</span>
            <br/>
          {/each} 
          
          <style> 
            .checked {
                  text-decoration: line-through;
              }
          </style>
        </div>
      </div>
    </TabItem>
    <TabItem open title="Low">
      <div class="container mx-auto max-w-lg h-[600px] p-4 border-solid border-black rounded-lg shadow-lg">
        <p class="text-2xl font-bold text-center font-pacifico">Todo</p>
        <div class="mx-auto">
          <input bind:value={newItem} type="text" placeholder="new todo item..">
          <button on:click={addToList}>Add</button>
          
          <br/>
          {#each todoList as item, index}
            <input bind:checked={item.status} type="checkbox">
            <span class:checked={item.status}>{item.text}</span>
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <span on:click={() => removeFromList(index)}>❌</span>
            <br/>
          {/each} 
          
          <style> 
            .checked {
                  text-decoration: line-through;
              }
          </style>
        </div>
      </div>
    </TabItem>
    <TabItem open title="Notes">
      <div class="container mx-auto max-w-lg h-[600px] p-4 border-solid border-black rounded-lg shadow-lg">
        <p class="text-2xl font-bold text-center font-pacifico">Notes</p>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quos error vero dolorem explicabo ab, architecto blanditiis optio excepturi mollitia veniam nobis natus! Non a quo iure perspiciatis esse accusantium! Ab?</p>
      </div>
    </TabItem>
  </Tabs>

  <!-- Card example
  <div class="max-w-sm mx-auto rounded overflow-hidden shadow-lg">
    <img class="w-full" src="https://v1.tailwindcss.com/img/card-top.jpg" alt="Sunset in the mountains">
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">The Coldest Sunset</div>
      <p class="text-gray-700 text-base">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.
      </p>
    </div>
    <div class="px-6 pt-4 pb-2">
      <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#photography</span>
      <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#travel</span>
      <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#winter</span>
    </div>
  </div> -->
</section>

<Footer>
  <FooterCopyright href="/" by="Flowbite™" year={2023} copyrightMessage="This is a test footer and needs to be stickied to the bottom" />
  <FooterLinkGroup ulClass="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
    <FooterLink href="/">About</FooterLink>
    <FooterLink href="/">Privacy Policy</FooterLink>
    <FooterLink href="/">Licensing</FooterLink>
    <FooterLink href="/">Contact</FooterLink>
  </FooterLinkGroup>
</Footer>