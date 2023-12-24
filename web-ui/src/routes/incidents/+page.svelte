<script lang="ts">
	import { page } from '$app/stores';

	console.log('Incident page loaded: ', $page.url.pathname);
</script>

<div class="container p-10 space-y-4">
	{#if $page.data.session}
		<h1>Incidents</h1>
		<hr />
		<p>
			Fireops is a ....
		</p>
	{:else}
		<h1>Access Denied</h1>
		<p>
			<a href="/auth/signin" data-sveltekit-preload-data="off">
				You must be signed in to view this page
			</a>
		</p>
	{/if}
</div>