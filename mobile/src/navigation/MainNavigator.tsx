import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import Icon from 'react-native-vector-icons/MaterialIcons';
import { useTranslation } from 'react-i18next';

// Import screens
import MarketplaceScreen from '../screens/marketplace/MarketplaceScreen';
import ProductDetailScreen from '../screens/marketplace/ProductDetailScreen';
import MyProductsScreen from '../screens/marketplace/MyProductsScreen';
import ChatListScreen from '../screens/chat/ChatListScreen';
import ChatScreen from '../screens/chat/ChatScreen';
import ProfileScreen from '../screens/profile/ProfileScreen';
import DiagnosticsScreen from '../screens/diagnostics/DiagnosticsScreen';

export type MainStackParamList = {
  MainTabs: undefined;
  ProductDetail: { productId: string };
  Chat: { conversationId: string; participantName: string };
};

export type MainTabParamList = {
  Marketplace: undefined;
  Chat: undefined;
  Diagnostics: undefined;
  Profile: undefined;
};

const Stack = createStackNavigator<MainStackParamList>();
const Tab = createBottomTabNavigator<MainTabParamList>();

const MainTabs: React.FC = () => {
  const { t } = useTranslation();

  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName: string;

          switch (route.name) {
            case 'Marketplace':
              iconName = 'store';
              break;
            case 'Chat':
              iconName = 'chat';
              break;
            case 'Diagnostics':
              iconName = 'local-hospital';
              break;
            case 'Profile':
              iconName = 'person';
              break;
            default:
              iconName = 'help';
          }

          return <Icon name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#2E7D32',
        tabBarInactiveTintColor: '#757575',
        headerShown: false,
      })}
    >
      <Tab.Screen 
        name="Marketplace" 
        component={MarketplaceScreen}
        options={{ tabBarLabel: t('navigation.marketplace') }}
      />
      <Tab.Screen 
        name="Chat" 
        component={ChatListScreen}
        options={{ tabBarLabel: t('navigation.chat') }}
      />
      <Tab.Screen 
        name="Diagnostics" 
        component={DiagnosticsScreen}
        options={{ tabBarLabel: t('navigation.diagnostics') }}
      />
      <Tab.Screen 
        name="Profile" 
        component={ProfileScreen}
        options={{ tabBarLabel: t('navigation.profile') }}
      />
    </Tab.Navigator>
  );
};

const MainNavigator: React.FC = () => {
  return (
    <Stack.Navigator>
      <Stack.Screen 
        name="MainTabs" 
        component={MainTabs}
        options={{ headerShown: false }}
      />
      <Stack.Screen 
        name="ProductDetail" 
        component={ProductDetailScreen}
        options={{ title: 'Ürün Detayı' }}
      />
      <Stack.Screen 
        name="Chat" 
        component={ChatScreen}
        options={({ route }) => ({ title: route.params.participantName })}
      />
    </Stack.Navigator>
  );
};

export default MainNavigator;