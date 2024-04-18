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
const huh = [{"url": "/paper_files/paper/2022/hash/002262941c9edfd472a79298b2ac5e17-Abstract-Conference.html", "name": "Federated Submodel Optimization for Hot and Cold Data Features"}, {"url": "/paper_files/paper/2022/hash/00295cede6e1600d344b5cd6d9fd4640-Abstract-Conference.html", "name": "On Kernelized Multi-Armed Bandits with Constraints"}, {"url": "/paper_files/paper/2022/hash/00358de35a101a372ea0412bed913c86-Abstract-Conference.html", "name": "Geometric Order Learning for Rank Estimation"}]
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
          <div
            style={{
              padding: 24,
              textAlign: 'center',
              background: colorBgContainer,
              borderRadius: borderRadiusLG,
            }}
          >
            <p>long content</p>
            {
              // indicates very long content
              Array.from(
                {
                  length: 3,
                },
                (_, index) => (
                  <React.Fragment key={index}>
                    {huh[index].url}
                    <br />
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