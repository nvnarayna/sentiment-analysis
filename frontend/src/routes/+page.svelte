<script lang='ts'>
    import Showcase from "$lib/Showcase.svelte";
    import { TabGroup, Tab, TabAnchor } from '@skeletonlabs/skeleton';
    import Explaination from "$lib/Explaination.svelte";
    let tabSet: number = 0;
    let redirect_git=()=>{
        window.open("https://github.com/nvnarayna/sentiment-analysis")
        tabSet=0
    }
</script>


<TabGroup justify="justify-center">
	<Tab bind:group={tabSet} name="tab1" value={0}>Try</Tab>
	<Tab bind:group={tabSet} name="tab2" value={1}>explaination</Tab>
	<Tab on:click={redirect_git} bind:group={tabSet} name="tab3" value={2}>Source Github</Tab>
	<!-- Tab Panels --->
	<svelte:fragment slot="panel">
		{#if tabSet === 0}
        <Showcase/>
        {:else if tabSet === 1}
        <Explaination/>
        {/if}
	</svelte:fragment>
</TabGroup>
			
