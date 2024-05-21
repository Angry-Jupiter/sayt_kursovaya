import React from 'react';
import {
  AppstoreOutlined,
  BarChartOutlined,
  CloudOutlined,
  ShopOutlined,
  TeamOutlined,
  UploadOutlined,
  UserOutlined,
  VideoCameraOutlined,
} from '@ant-design/icons';
import { Layout, Menu, theme } from 'antd';


const { Header, Content, Footer, Sider } = Layout;
const items = [
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
  BarChartOutlined,
  CloudOutlined,
  AppstoreOutlined,
  TeamOutlined,
  ShopOutlined,
].map((icon, index) => ({
  key: String(index + 1),
  icon: React.createElement(icon),
  label: `nav ${index + 1}`,
}));

const huh = require('./data.json');
console.log(huh);

const App = () => {
  
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();
  return (
    <Layout hasSider>
      <Sider
        style={{
          overflow: 'auto',
          height: '100vh',
          position: 'fixed',
          left: 0,
          top: 0,
          bottom: 0,
        }}
      >
        <div className="demo-logo-vertical" />
        <Menu theme="dark" mode="inline" defaultSelectedKeys={['4']} items={items} />
      </Sider>
      <Layout
        style={{
          marginLeft: 200,
        }}
      >
        <Header
          style={{
            padding: 0,
            background: colorBgContainer,
          }}
        />
        <Content
          style={{
            margin: '24px 16px 0',
            overflow: 'initial',
          }}
        >
          <div style={{padding: 24, textAlign: 'central', background: colorBgContainer, borderRadius: borderRadiusLG,}}><h3>Articles I recommend reading! </h3></div>
          <div
            style={{
              padding: 24,
              textAlign: 'left',
              background: colorBgContainer,
              borderRadius: borderRadiusLG,
            }}
          >
            {
              // indicates very long content
              Array.from(
                {
                  length: 50,
                },
                (_, index) => ( 
                  <React.Fragment key={index}>
                    <a href = {huh[index].url}>
                    {huh[index].name}
                    </a><br/>
                    <p><a href = {huh[index].url2}>Authors:{huh[index].authors}</a></p>
                    <br/>
                    <p>Is Good:{huh[index].isGood}</p>
                    <br /><br />
                  </React.Fragment>
                ),
              )
            }
          </div>
        </Content>
        <Footer
          style={{
            textAlign: 'center',
          }}
        >
          Ant Design ©{new Date().getFullYear()} Created by Sofka_drunk
        </Footer>
      </Layout>
    </Layout>
  );
};
export default App;