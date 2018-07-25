import {
    createStackNavigator,
  } from 'react-navigation';

import Login from './Login';
import Buttons from './Buttons';

  const App = createStackNavigator({
      Home: {
          screen: Login,
        },
      Buttons: {screen: Buttons},

  }, {headerMode: 'none',
  navigationOptions: {
      headerVisible: false
  }})

  export default App;
