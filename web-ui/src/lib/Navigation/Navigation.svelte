<script lang="ts">
	import { getDrawerStore } from "@skeletonlabs/skeleton";

	const drawerStore = getDrawerStore();

	function drawerClose(): void {
		drawerStore.close();
	}
</script>

<li><a href="/" on:click={drawerClose}>Homepage</a></li>
<li><a href="/incidents" on:click={drawerClose}>Incidents</a></li>
<li><a href="/about" on:click={drawerClose}>About</a></li>
<li><a href="/contact" on:click={drawerClose}>Contact</a></li>

<button class="lg:hidden btn btn-sm mr-4" on:click={drawerClose}>X</button>
