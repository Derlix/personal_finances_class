<script setup>
import SideBar from '../src/components/DashBoard/SideBar.vue'
</script>

<template>
    <!-- Page Wrapper -->
    <div id="wrapper">
        <SideBar></SideBar>
    </div>

    <div>
        <div>
            <TopBar></TopBar>
            <BlankPage />
        </div>
        <FooterCom />
    </div>
</template>

