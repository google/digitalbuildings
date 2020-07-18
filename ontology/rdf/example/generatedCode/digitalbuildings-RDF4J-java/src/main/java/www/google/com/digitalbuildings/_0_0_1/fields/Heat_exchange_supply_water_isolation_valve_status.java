package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IExchange;
import www.google.com.digitalbuildings._0_0_1.subfields.Exchange;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.Status;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.Water;
import www.google.com.digitalbuildings._0_0_1.subfields.IHeat;
import www.google.com.digitalbuildings._0_0_1.subfields.Heat;
import www.google.com.digitalbuildings._0_0_1.subfields.ISupply;
import www.google.com.digitalbuildings._0_0_1.subfields.Supply;
import www.google.com.digitalbuildings._0_0_1.subfields.IIsolation;
import www.google.com.digitalbuildings._0_0_1.subfields.Isolation;
import www.google.com.digitalbuildings._0_0_1.subfields.IValve;
import www.google.com.digitalbuildings._0_0_1.subfields.Valve;


@SuppressWarnings("serial")
public class Heat_exchange_supply_water_isolation_valve_status extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IHeat_exchange_supply_water_isolation_valve_status{

	IRI newInstance;
	public Heat_exchange_supply_water_isolation_valve_status(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Heat_exchange_supply_water_isolation_valve_status"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfExchange (IExchange parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IExchange> getComposedOfExchange (){
		Set<IExchange> ComposedOfExchange = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Exchange) {
				ComposedOfExchange.add((Exchange)action);
			}
		});
		return ComposedOfExchange;
	}


  public void addComposedOfHeat (IHeat parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IHeat> getComposedOfHeat (){
		Set<IHeat> ComposedOfHeat = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Heat) {
				ComposedOfHeat.add((Heat)action);
			}
		});
		return ComposedOfHeat;
	}


  public void addComposedOfIsolation (IIsolation parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IIsolation> getComposedOfIsolation (){
		Set<IIsolation> ComposedOfIsolation = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Isolation) {
				ComposedOfIsolation.add((Isolation)action);
			}
		});
		return ComposedOfIsolation;
	}


  public void addComposedOfStatus (IStatus parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IStatus> getComposedOfStatus (){
		Set<IStatus> ComposedOfStatus = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Status) {
				ComposedOfStatus.add((Status)action);
			}
		});
		return ComposedOfStatus;
	}


  public void addComposedOfSupply (ISupply parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISupply> getComposedOfSupply (){
		Set<ISupply> ComposedOfSupply = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Supply) {
				ComposedOfSupply.add((Supply)action);
			}
		});
		return ComposedOfSupply;
	}


  public void addComposedOfValve (IValve parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IValve> getComposedOfValve (){
		Set<IValve> ComposedOfValve = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Valve) {
				ComposedOfValve.add((Valve)action);
			}
		});
		return ComposedOfValve;
	}


  public void addComposedOfWater (IWater parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IWater> getComposedOfWater (){
		Set<IWater> ComposedOfWater = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Water) {
				ComposedOfWater.add((Water)action);
			}
		});
		return ComposedOfWater;
	}

	public static Set<IHeat_exchange_supply_water_isolation_valve_status> getAllHeat_exchange_supply_water_isolation_valve_statussObjectsCreated(){
		Set<IHeat_exchange_supply_water_isolation_valve_status> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Heat_exchange_supply_water_isolation_valve_status")).subjects().stream()
		.map(mapper->(IHeat_exchange_supply_water_isolation_valve_status)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}