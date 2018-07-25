import React from 'react';
import {StyleSheet, Text, View, TextInput, Button, Image} from 'react-native';

export default class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'host': '0.0.0.0'
		}

    }

	static navigationOptions = {
		title: "U-tonera"
	}

    render() {

		const { navigate } = this.props.navigation

        return (
            <View style={styles.container}>
                <View style={{flex: 2}}>
                    <Image
                        source={require("./static/logo.png")}
                        style={{flex:1, resizeMode:'contain', width: 300, height: 300}}
                        />
                </View>
                <View style={{flex: 3}}>
                    <Text style={{color: "#fff"}}>Ingresa la URL del dominio</Text>
                    <TextInput
                        onChangeText={(text) => this.setState({host: text})}
                        style={styles.inputStyle}
                        blurOnSubmit={false}
                    />
                    <Button
                        title="Ingresar"
                        onPress={ () =>
                            navigate('Buttons', {host: this.state.host})
                        }
                    />
                </View>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#3A5D83',
        alignItems: 'center',
        justifyContent: 'center'
    },

    inputStyle: {
        width: 250,
        color: "#fff"
    }
});
