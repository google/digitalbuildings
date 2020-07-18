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
* Class Dmp_edm 
* Exhaust damper monitoring.
*/
@SuppressWarnings("serial")
public class Dmp_edm extends www.google.com.digitalbuildings._0_0_1.hvac.Dmp implements IDmp_edm{

	IRI newInstance;
	public Dmp_edm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_edm"));
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

	public static Set<IDmp_edm> getAllDmp_edmsObjectsCreated(){
		Set<IDmp_edm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_edm")).subjects().stream()
		.map(mapper->(IDmp_edm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}