package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_status_1;

/**
* Class Cdws_us_mtv_2081_1 
* Non-standard 2081 CDWS
*/
@SuppressWarnings("serial")
public class Cdws_us_mtv_2081_1 extends www.google.com.digitalbuildings._0_0_1.hvac.Cdws implements ICdws_us_mtv_2081_1{

	IRI newInstance;
	public Cdws_us_mtv_2081_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdws_us_mtv_2081_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesReturn_water_isolation_valve_status_1 (IReturn_water_isolation_valve_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_status_1> getUsesReturn_water_isolation_valve_status_1 (){
		Set<IReturn_water_isolation_valve_status_1> UsesReturn_water_isolation_valve_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_status_1) {
				UsesReturn_water_isolation_valve_status_1.add((Return_water_isolation_valve_status_1)action);
			}
		});
		return UsesReturn_water_isolation_valve_status_1;
	}


  public void addUsesReturn_water_isolation_valve_status_2 (IReturn_water_isolation_valve_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_status_2> getUsesReturn_water_isolation_valve_status_2 (){
		Set<IReturn_water_isolation_valve_status_2> UsesReturn_water_isolation_valve_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_status_2) {
				UsesReturn_water_isolation_valve_status_2.add((Return_water_isolation_valve_status_2)action);
			}
		});
		return UsesReturn_water_isolation_valve_status_2;
	}


  public void addUsesReturn_water_isolation_valve_status_3 (IReturn_water_isolation_valve_status_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_status_3> getUsesReturn_water_isolation_valve_status_3 (){
		Set<IReturn_water_isolation_valve_status_3> UsesReturn_water_isolation_valve_status_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_status_3) {
				UsesReturn_water_isolation_valve_status_3.add((Return_water_isolation_valve_status_3)action);
			}
		});
		return UsesReturn_water_isolation_valve_status_3;
	}


  public void addUsesReturn_water_isolation_valve_status_4 (IReturn_water_isolation_valve_status_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_status_4> getUsesReturn_water_isolation_valve_status_4 (){
		Set<IReturn_water_isolation_valve_status_4> UsesReturn_water_isolation_valve_status_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_status_4) {
				UsesReturn_water_isolation_valve_status_4.add((Return_water_isolation_valve_status_4)action);
			}
		});
		return UsesReturn_water_isolation_valve_status_4;
	}


  public void addUsesSupply_water_isolation_valve_status_1 (ISupply_water_isolation_valve_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_status_1> getUsesSupply_water_isolation_valve_status_1 (){
		Set<ISupply_water_isolation_valve_status_1> UsesSupply_water_isolation_valve_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_status_1) {
				UsesSupply_water_isolation_valve_status_1.add((Supply_water_isolation_valve_status_1)action);
			}
		});
		return UsesSupply_water_isolation_valve_status_1;
	}


  public void addUsesSupply_water_isolation_valve_status_2 (ISupply_water_isolation_valve_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_status_2> getUsesSupply_water_isolation_valve_status_2 (){
		Set<ISupply_water_isolation_valve_status_2> UsesSupply_water_isolation_valve_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_status_2) {
				UsesSupply_water_isolation_valve_status_2.add((Supply_water_isolation_valve_status_2)action);
			}
		});
		return UsesSupply_water_isolation_valve_status_2;
	}


  public void addUsesSupply_water_isolation_valve_status_3 (ISupply_water_isolation_valve_status_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_status_3> getUsesSupply_water_isolation_valve_status_3 (){
		Set<ISupply_water_isolation_valve_status_3> UsesSupply_water_isolation_valve_status_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_status_3) {
				UsesSupply_water_isolation_valve_status_3.add((Supply_water_isolation_valve_status_3)action);
			}
		});
		return UsesSupply_water_isolation_valve_status_3;
	}


  public void addUsesSupply_water_isolation_valve_status_4 (ISupply_water_isolation_valve_status_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_status_4> getUsesSupply_water_isolation_valve_status_4 (){
		Set<ISupply_water_isolation_valve_status_4> UsesSupply_water_isolation_valve_status_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_status_4) {
				UsesSupply_water_isolation_valve_status_4.add((Supply_water_isolation_valve_status_4)action);
			}
		});
		return UsesSupply_water_isolation_valve_status_4;
	}

	public static Set<ICdws_us_mtv_2081_1> getAllCdws_us_mtv_2081_1sObjectsCreated(){
		Set<ICdws_us_mtv_2081_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdws_us_mtv_2081_1")).subjects().stream()
		.map(mapper->(ICdws_us_mtv_2081_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}