<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
  <a-table :columns="columns" :data-source="table_data">
    <template #headerCell="{ column }">
      <template v-if="column.key === 'name'">
        <span>
          <smile-outlined/>
          Name
        </span>
      </template>
    </template>

    <template #bodyCell="{ column, record }">
      <template v-if="column.key === 'name'">
        <a>
          {{ record.name }}
        </a>
      </template>
      <template v-else-if="column.key === 'tags'">
        <span>
          <a-tag
              v-for="tag in record.tags"
              :key="tag"
              :color="tag === 'loser' ? 'volcano' : tag.length > 5 ? 'geekblue' : 'green'"
          >
            {{ tag.toUpperCase() }}
          </a-tag>
        </span>
      </template>
      <template v-else-if="column.key === 'action'">
        <span>
          <a>Invite 一 {{ record.name }}</a>
          <a-divider type="vertical"/>
          <a>Delete</a>
          <a-divider type="vertical"/>
          <a class="ant-dropdown-link">
            More actions
            <down-outlined/>
          </a>
        </span>
      </template>
    </template>
  </a-table>
  <a-row>
    <a-col :span="12">
      <div class="chart" ref="chart">

      </div>
    </a-col>
  </a-row>
</template>
<script>
import axios from "axios";
import * as echarts from 'echarts';
import {ref} from "vue";

export default {
  data() {
    return {
      columns: [
          {
        name: 'Name',
        dataIndex: 'name',
        key: 'name',
      },
        {
        title: 'Age',
        dataIndex: 'age',
        key: 'age',
      },
        {
        title: 'Address',
        dataIndex: 'address',
        key: 'address',
      },
        {
        title: 'Tags',
        key: 'tags',
        dataIndex: 'tags',
      },
        {
        title: 'Action',
        key: 'action',
      }],
      table_data: [
        {
        key: '1',
        name: 'John Brown',
        age: 32,
        address: 'New York No. 1 Lake Park',
        tags: ['nice', 'developer'],
      },
        {
        key: '2',
        name: 'Jim Green',
        age: 42,
        address: 'London No. 1 Lake Park',
        tags: ['loser'],
      },
        {
        key: '3',
        name: 'Joe Black',
        age: 32,
        address: 'Sidney No. 1 Lake Park',
        tags: ['cool', 'teacher'],
      }]




    }
  },

  methods:{
    chat(){
      console.log(this.$refs.chart)
      var myChart = echarts.init(this.$refs.chart);
      var option;

      option = {
        title: {
          text: 'Basic Radar Chart'
        },
        legend: {
          data: ['Allocated Budget', 'Actual Spending']
        },
        radar: {
          // shape: 'circle',
          indicator: [
            {name: 'Sales', max: 6500},
            {name: 'Administration', max: 16000},
            {name: 'Information Technology', max: 30000},
            {name: 'Customer Support', max: 38000},
            {name: 'Development', max: 52000},
            {name: 'Marketing', max: 25000}
          ]
        },
        series: [
          {
            name: 'Budget vs spending',
            type: 'radar',
            data: [
              {
                value: [4200, 3000, 20000, 35000, 50000, 18000],
                name: 'Allocated Budget'
              }
            ]
          }
        ]
      };

      option && myChart.setOption(option);
    }

  },

  mounted() {
    this.chat()
  }
}
</script>

<style>
.chart{
  height: 500px;
}
</style>