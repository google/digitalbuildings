package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_status;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_command;

/**
* Class Fan_us_svl_brg1_2 
* Non-standard type for BRG1
*/
@SuppressWarnings("serial")
public class Fan_us_svl_brg1_2 extends www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss implements IFan_us_svl_brg1_2{

	IRI newInstance;
	public Fan_us_svl_brg1_2(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_brg1_2"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesExhaust_air_damper_command (IExhaust_air_damper_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_damper_command> getUsesExhaust_air_damper_command (){
		Set<IExhaust_air_damper_command> UsesExhaust_air_damper_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_damper_command) {
				UsesExhaust_air_damper_command.add((Exhaust_air_damper_command)action);
			}
		});
		return UsesExhaust_air_damper_command;
	}


  public void addUsesExhaust_air_damper_status (IExhaust_air_damper_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_damper_status> getUsesExhaust_air_damper_status (){
		Set<IExhaust_air_damper_status> UsesExhaust_air_damper_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_damper_status) {
				UsesExhaust_air_damper_status.add((Exhaust_air_damper_status)action);
			}
		});
		return UsesExhaust_air_damper_status;
	}

	public static Set<IFan_us_svl_brg1_2> getAllFan_us_svl_brg1_2sObjectsCreated(){
		Set<IFan_us_svl_brg1_2> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_brg1_2")).subjects().stream()
		.map(mapper->(IFan_us_svl_brg1_2)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}