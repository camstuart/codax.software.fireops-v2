<script lang="ts">
	import { page } from '$app/stores';

	console.log('Incident page loaded: ', $page.url.pathname);


	import { onMount } from 'svelte';

	let incidents = [];
	let error = null;

	async function fetchIncidents() {
		try {
			const response = await fetch('http://localhost:3000/api/incidents');
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			incidents = await response.json();
		} catch (err) {
			error = err.message;
		}
	}

	onMount(fetchIncidents);


</script>

<div class="container p-10 space-y-4">
	{#if $page.data.session}
		<h1>Incidents</h1>
		<hr />
		{#if error}
			<p>Error: {error}</p>
		{:else}
			<ul>
				{#each incidents as incident}
					<li>{incident.name} - {incident.description}</li>
				{/each}
			</ul>
		{/if}
	{:else}
		<h1>Access Denied</h1>
		<p>
			<a href="/auth/signin" data-sveltekit-preload-data="off">
				You must be signed in to view this page
			</a>
		</p>
	{/if}
</div>