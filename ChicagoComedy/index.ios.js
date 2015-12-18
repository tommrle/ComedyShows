/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 */
'use strict';

var React = require('react-native');
var {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  ListView,
  PixelRatio,
  Image,
  NavigatorIOS,
  TouchableHighlight
} = React;

var ShowView = require('./tabs/ShowView');

var ChicagoComedyB = React.createClass({
  componentWillMount: function() {
    fetch('http://localhost:8080/allshows')
      .then(res => res.json())
      .then(res => this.updateDataSource(res));
  },
  getInitialState: function() {
    return {
      dataSource: new ListView.DataSource({
        rowHasChanged: (r1, r2) => r1 !== r2
      })
    };
  },
  updateDataSource: function(data) {
    this.setState({
      dataSource: this.state.dataSource.cloneWithRows(data)
    })
  },
  openShow: function (show) {
    this.props.navigator.push({
      title: 'Details',
      component: ShowView,
      passProps: { show }
    });
  },
  renderRow: function(show) {
    var imageUrl = 'http://localhost:8080/' + show.imageUrl;
    console.log("rendering row");
    return (
      <View>
        <TouchableHighlight onPress={ this.openShow.bind(this, show) }>
          <View>
            <View style={ styles.row }>
              <Image source={{ uri: imageUrl }}
                    style={ styles.cellImage } />
              <View style={ styles.textContainer }>
                <Text style={ styles.title } numberOfLines={ 1 }>
                  { show.title }
                </Text>
                <Text style = { styles.price } numberOfLines={ 1 }>
                  { show.ticketPriceRange }
                </Text>
                <Text style={ styles.description } numberOfLines={ 1 }>
                  { show.descrip }
                </Text>
              </View>
            </View>
            <View style={ styles.cellBorder } />
          </View>
        </TouchableHighlight>
      </View>
    );
  },
  render: function() {
    return (
      <View style={ styles.container }>
        <ListView
          dataSource={this.state.dataSource}
          renderRow={ this.renderRow } />
      </View>
    );
  }
});

            //component: ChicagoComedyB

var ChicagoComedy = React.createClass({
  render: function() {
    return (
      <NavigatorIOS
        style={ styles.container }
        initialRoute={
          {
            title: 'Chicago Comedy',
            component: ShowView
          }
        } />
    );
  }
});

var styles = StyleSheet.create({
  container: {
    flex: 1
  },
  row: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: 'white',
    flexDirection: 'row',
    padding: 10
  },
  textContainer: {
    flex: 1
  },
  cellImage: {
    height: 60,
    borderRadius: 30,
    marginRight: 10,
    width: 60
  },
  title: {
    flex: 1,
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 2
  },
  description: {
    color: '#999999',
    fontSize: 12
  },
  header: {
    height: 50,
    backgroundColor: '#760004',
    paddingTop: 20,
    alignItems: 'center'
  },
  headerText: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold'
  },
  cellBorder: {
    backgroundColor: '#F2F2F2',
    height: 1 / PixelRatio.get(),
    marginLeft: 4
  },
  price: {
    position: 'absolute',
    top: 0,
    right: 0,
    fontSize: 12,
    color: '#cccccc'
  }
});

AppRegistry.registerComponent('ChicagoComedy', () => ChicagoComedy);
