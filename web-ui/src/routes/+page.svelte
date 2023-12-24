<script lang="ts">
	import { page } from '$app/stores';
	console.log("Home (index) page loaded: ", $page.url.pathname);
</script>

<div class="container p-10 space-y-4">
	<h1>Homepage</h1>
	<hr />
	<p>
		The homepage has been setup so no sidebar navigation is visible on desktop screens. However if you resize or view on smaller mobile size
		devices, a hamburger menu will appear, allowing you to access the standard navigation.
	</p>
</div>