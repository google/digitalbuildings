package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixing_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Mixing_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_temperature_setpoint;

/**
* Class Pmp_s_vscf_isv 
* One-off pump that performs chilled water blending.
*/
@SuppressWarnings("serial")
public class Pmp_s_vscf_isv extends www.google.com.digitalbuildings._0_0_1.hvac.Pmp_ss_vsc implements IPmp_s_vscf_isv{

	IRI newInstance;
	public Pmp_s_vscf_isv(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pmp_s_vscf_isv"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesMixing_valve_percentage_command (IMixing_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMixing_valve_percentage_command> getUsesMixing_valve_percentage_command (){
		Set<IMixing_valve_percentage_command> UsesMixing_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Mixing_valve_percentage_command) {
				UsesMixing_valve_percentage_command.add((Mixing_valve_percentage_command)action);
			}
		});
		return UsesMixing_valve_percentage_command;
	}

	public static Set<IPmp_s_vscf_isv> getAllPmp_s_vscf_isvsObjectsCreated(){
		Set<IPmp_s_vscf_isv> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pmp_s_vscf_isv")).subjects().stream()
		.map(mapper->(IPmp_s_vscf_isv)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}