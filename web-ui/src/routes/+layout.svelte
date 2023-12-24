<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
	import { initializeStores, Drawer, getDrawerStore } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';


	// Floating UI for Popups
	import { computePosition, autoUpdate, flip, shift, offset, arrow } from '@floating-ui/dom';
	import { storePopup } from '@skeletonlabs/skeleton';
	import Navigation from '$lib/Navigation/Navigation.svelte';
	storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });

	initializeStores();

	const drawerStore = getDrawerStore();

	function drawerOpen(): void {
		drawerStore.open({});
	}


	$: classesSidebar = $page.url.pathname === '/' ? 'w-0' : 'w-0 lg:w-64';

</script>

<Drawer>
	<Navigation />
</Drawer>

<!-- App Shell -->
<AppShell slotSidebarLeft="bg-surface-500/5 w-0 lg:w-64 {classesSidebar}">
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<div class="flex items-center">
					<button class="lg:hidden btn btn-sm mr-4" on:click={drawerOpen}>
            <span>
                <svg viewBox="0 0 100 80" class="fill-token w-4 h-4">
                    <rect width="100" height="20" />
                    <rect y="30" width="100" height="20" />
                    <rect y="60" width="100" height="20" />
                </svg>
            </span>
					</button>
					<strong class="text-xl uppercase">Skeleton</strong>
				</div>
			</svelte:fragment>
			<svelte:fragment slot="trail">
				{#if $page.data.session} {#if $page.data.session.user?.image}
					<span
						style="background-image: url('{$page.data.session.user.image}')"
						class="avatar"
					/>
				{/if}

					<span>
						<small>Signed in as</small>
						<br />
						<strong>
							{$page.data.session.user?.email ?? $page.data.session.user?.name}
						</strong>
					</span>

					<a href="/auth/signout" class="button" data-sveltekit-preload-data="off">
						Sign out
					</a>
				{:else}
					<span class="notSignedInText"> You are not signed in </span>

					<a href="/auth/signin" class="buttonPrimary" data-sveltekit-preload-data="off">
						Sign in
					</a>
				{/if}
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>

	<svelte:fragment slot="sidebarLeft">
		<div class="h-full">
			<Navigation />
		</div>
	</svelte:fragment>

	<!-- Page Route Content -->
	<slot />

	<svelte:fragment slot="pageFooter">Page Footer</svelte:fragment>

</AppShell>
