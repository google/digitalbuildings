package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_isolation_damper_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_isolation_damper_command;

/**
* Class Vav_us_pao_mir3_2 
* Non-standard type for MIR3
*/
@SuppressWarnings("serial")
public class Vav_us_pao_mir3_2 extends www.google.com.digitalbuildings._0_0_1.hvac.Vav_sd_csp implements IVav_us_pao_mir3_2{

	IRI newInstance;
	public Vav_us_pao_mir3_2(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Vav_us_pao_mir3_2"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSupply_air_isolation_damper_command (ISupply_air_isolation_damper_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_isolation_damper_command> getUsesSupply_air_isolation_damper_command (){
		Set<ISupply_air_isolation_damper_command> UsesSupply_air_isolation_damper_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_isolation_damper_command) {
				UsesSupply_air_isolation_damper_command.add((Supply_air_isolation_damper_command)action);
			}
		});
		return UsesSupply_air_isolation_damper_command;
	}

	public static Set<IVav_us_pao_mir3_2> getAllVav_us_pao_mir3_2sObjectsCreated(){
		Set<IVav_us_pao_mir3_2> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Vav_us_pao_mir3_2")).subjects().stream()
		.map(mapper->(IVav_us_pao_mir3_2)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}