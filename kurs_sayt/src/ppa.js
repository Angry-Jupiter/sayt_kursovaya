import React, { useState } from 'react';
import { TreeSelect } from 'antd';
const treeData = [
  {
    title: 'Federated Submodel Optimization for Hot and Cold Data Features',
    value: '0-1',
  },
  {
    title: 'Adaptive Interest for Emphatic Reinforcement Learning',
    value: '0-1',
  },
  {
    title: 'SatMAE: Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery',
    value: '0-2',
  },
];
const App1 = () => {
  const [value, setValue] = useState();
  const onChange = (newValue) => {
    console.log(newValue);
    setValue(newValue);
  };
  return (
    <TreeSelect
      style={{
        width: '100%',
      }}
      value={value}
      dropdownStyle={{
        maxHeight: 400,
        overflow: 'auto',
      }}
      treeData={treeData}
      placeholder="Please select"
      treeDefaultExpandAll
      onChange={onChange}

      showSearch 
      treeNodeFilterProp='Federated Submodel Optimization for Hot and Cold Data Features' 
      treeData={treeData}
    />
  );
};
export default App1;