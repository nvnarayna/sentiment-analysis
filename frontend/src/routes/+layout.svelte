<script lang="ts">
	import '../app.postcss';
	import { AppShell } from '@skeletonlabs/skeleton';
	import { AppBar } from '@skeletonlabs/skeleton';
</script>

<AppShell>
	<svelte:fragment slot="header">
		<AppBar gridColumns="grid-cols-3" slotDefault="place-self-center" slotTrail="place-content-end">
			<svelte:fragment slot="lead"><p>nvn</p></svelte:fragment>
			<h1 class='h3'>projects</h1>
			<svelte:fragment slot="trail">settings</svelte:fragment>
		</AppBar>		
	</svelte:fragment>

	<slot />
</AppShell>

